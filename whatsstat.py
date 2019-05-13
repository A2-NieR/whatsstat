#! python3
# WhatsStat.py - Analyses a .txt export (without media) of a Whatsapp chat history,
# prints a wordcloud and charts for dates and times.

from csv import reader
import datetime
import os

import func

# libraries for visualization
import numpy as np
import pylab as pl
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from wordcloud import WordCloud, STOPWORDS  # , ImageColorGenerator
import matplotlib.pyplot as plt
plt.rcdefaults()


while True:
    try:
        file = input("Please enter the path to the .txt-file: ")
        opened_file = open(file)
    except OSError:
        print("Error: File not found. Check path & filename.")
    else:
        break

read_file = reader((line.replace("\0", "") for line in opened_file))
chat = list(read_file)
chat2 = []

# delete empty lines in text
for row in chat:
    if row != []:
        chat2.append(row)

chat_header = chat2[0]
chat_main = chat2[1:]

func.extract_nodate(chat_main)
func.clean_nodate(func.chat_without_date)
func.pull(func.chat_with_date)
func.open_list(func.msg_only)

# merge messages into one file
msgs = func.msg + func.msg_open

func.extract_emojis(msgs)    # TODO: Find a way to use the extracted emojis
func.remove_nonletters(msgs)

func.caps(func.messages_final)
func.singled(func.cpt_caps)

text = " ".join(func.single_words)
# special = " ".join(ems)
# specials = special.encode('utf-8')

func.convert_date(func.date)
# convert_time(time)

print("There are {} words in your chat.".format(len(text)))
# print("There are {} emojis in your chat.".format(len(specials)))


# sort dates & times + create dictionaries
func.sort_days(func.wdays, "Mon")
func.sort_days(func.wdays, "Tue")
func.sort_days(func.wdays, "Wed")
func.sort_days(func.wdays, "Thu")
func.sort_days(func.wdays, "Fri")
func.sort_days(func.wdays, "Sat")
func.sort_days(func.wdays, "Sun")

# extract keys&values from weekdays dictionary
d_obj = []
d_perf = []

for k in func.d_count.keys():
    d_obj.append(k)

for n in func.d_count.values():
    d_perf.append(n)


# extract keys&values from dictionary (from extracted times)
t_count = {}

func.clock.sort()

for t in func.clock:
    t_count.setdefault(t, 0)
    t_count[t] = t_count[t] + 1

t_key = t_count.keys()
t_val = t_count.values()

t_time = []

for item in t_key:  # convert time strings to datetime format
    item = datetime.datetime.strptime(item, "%H:%M").time()
    t_time.append(item)


# Generate & save weekdays bar chart
y_pos = np.arange(len(func.d_count))

fig = plt.figure()
plt.bar(y_pos, d_perf, align="center", alpha=0.5)
plt.xticks(y_pos, d_obj)
plt.ylabel('# of messages')
plt.title('Busiest days:')
fig.savefig("days.png", dpi=200)


# Generate & save time line chart
fig = plt.figure()

x = t_time
y = t_val

pl.xlabel("")
pl.ylabel("# of messages")
pl.title("Busiest times:")
ax = plt.gca()
# set x-axis to 0-24h, can most likely be improved
hours = [datetime.time(0, 0), datetime.time(1, 0), datetime.time(2, 0),
         datetime.time(3, 0), datetime.time(4, 0), datetime.time(5, 0),
         datetime.time(6, 0), datetime.time(7, 0), datetime.time(8, 0),
         datetime.time(9, 0), datetime.time(10, 0), datetime.time(11, 0),
         datetime.time(12, 0), datetime.time(13, 0), datetime.time(14, 0),
         datetime.time(15, 0), datetime.time(16, 0), datetime.time(17, 0),
         datetime.time(18, 0), datetime.time(19, 0), datetime.time(20, 0),
         datetime.time(21, 0), datetime.time(22, 0), datetime.time(23, 0),
         datetime.time(23, 59)]

ax.set_xticks(hours)
plt.xticks(fontsize=7)
plt.gcf().autofmt_xdate()
plt.plot(x, y, linewidth=0.5)
fig.savefig("times.png", dpi=200)


# TODO: Ask user to exclude stopwords
# Create stopword list
stopwords = set(STOPWORDS)

with open("stopwords.txt") as osw:
    sw = [line.strip(",\n'") for line in osw]
    sw = [line.upper() for line in sw]
    sw = [line.split() for line in sw]

stopw = []
for sublist in sw:
    for item in sublist:
        stopw.append(item)

stopwords.update(stopw)

print("Generating Wordcloud & Charts. Please wait…")

# wordcloud mask from file
wa_mask = np.array(Image.open("icons/wa_icon.png"))

# Create and generate a wordcloud
wordcloud = WordCloud(mask=wa_mask, stopwords=None, max_words=500,
                      max_font_size=200, background_color='white', font_path="Roboto_Black.ttf")

wordcloud.generate(text)
wordcloud.to_file("wc.png")

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(wa_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")


func.merge_image("days.png", "times.png", vertically=True)
func.merge_image("wc.png", "stats.png", vertically=False)


os.remove("days.png")
os.remove("times.png")

os.remove("wc.png")

# add current date to top left on final image
image = Image.open("stats.png")
font_type = ImageFont.truetype("Roboto_Black.ttf", 20)
draw = ImageDraw.Draw(image)
current_date = func.date[-1]
draw.text(xy=(70, 70), text=("Most frequent words & stats as of: " +
                             current_date), fill=(0, 0, 0), font=font_type)
image.save("final.png")

os.remove("stats.png")

print("Done. Enjoy your stats! :)")
