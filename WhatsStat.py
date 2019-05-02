#! python3
# WhatsStat.py - Analyses a .txt export (without media) of a Whatsapp chat history,
# prints a wordcloud and charts for dates and times.

from csv import reader
import re
import emoji
import datetime
import time
import regex
import os

# libraries for visualization
import numpy as np
import pandas as pd
import PIL
from PIL import Image, ImageDraw, ImageFont
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from pylab import *
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

read_file = reader(opened_file)
chat = list(read_file)
chat2 = []

# delete empty lines in text
for row in chat:
    if row != []:
        chat2.append(row)

chat_header = chat2[0]
chat_main = chat2[1:]


# check number of rows&columns of dataset
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n')  # adds a new (empty) line between rows

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


chat_with_date = []
chat_without_date = []


# store lines with messages only in separate list
def extract_nodate(database):
    for row in database:
        if len(row) == 1:
            chat_without_date.append(row)
        else:
            chat_with_date.append(row)


msg_only = []


# remove "., .., ..." from message only list + store in new list
def clean_nodate(dataset):
    for row in dataset:
        # row = list(row)
        for i in row:
            if i.startswith("."):
                continue
            else:
                msg_only.append(row)


date = []
clock = []
msg = []


# store items in separate lists & remove names
def pull(dataset):
    for row in dataset:
        row = list(row)
        # pull dates only in list, send other items to msg
        if len(row[0]) == 8 and row[0][1].isdecimal():
            date.append(row[0])
        else:
            msg.append(row[0])
        # pull times only in list
        if row[1][1:2].isdecimal() and row[1][3] == ":":
            clock.append(row[1][1:6])
        else:
            continue
        # remove names and pull messages in list
        item = row[1]
        try:
            # names are between " -" and a ":". Added so they get removed, too
            name = " -" + re.search(r"(?<= -).*?(?=:)", item).group(0) + ":"
        except AttributeError:
            name = ""
        item = item.replace(name, "")
        msg.append(item[7:])


msg_open = []


def open_list(dataset):
    for row in dataset:
        row = row[0]
        msg_open.append(row)


ems = []


# pull emojis in separate list
def extract_emojis(database):
    for row in database:
        text = regex.findall(r'\X', row)
        for word in text:
            if any(char in emoji.UNICODE_EMOJI for char in word):
                ems.append(word)


messages_final = []


# remove emojis, numbers, special characters & strip whitespace
def remove_nonletters(dataset):
    for row in dataset:
        regex = re.compile('[^a-zA-ZäöüÄÖÜß]')
        words = (regex.sub(' ', row))
        words = words.strip()
        # remove empty items, urls & <media excluded> message
# TODO: Add international no media messages
        if words == "" or words.startswith("http") or words == "Medien ausgeschlossen":
            continue
        else:
            messages_final.append(words)


cpt_caps = []


# Captain Caps to the rescue! Make everything WAMBO!
def caps(dataset):
    for item in dataset:
        cap = item.upper()
        cpt_caps.append(cap)


single_words = []


# pull every word into separate list
def singled(dataset):
    for item in dataset:
        item = item.split()
        for i in item:
            # remove single letters
            if len(i) == 1:
                continue
            else:
                single_words.append(i)


extract_nodate(chat_main)
clean_nodate(chat_without_date)
pull(chat_with_date)
open_list(msg_only)

# merge messages into one file
msgs = msg + msg_open

extract_emojis(msgs)    # TODO: Find a way to use the extracted emojis
remove_nonletters(msgs)

caps(messages_final)
singled(cpt_caps)

text = " ".join(single_words)
# special = " ".join(ems)
# specials = special.encode('utf-8')

wdays = []


def convert_date(dataset):
    for string in dataset:
        day = datetime.datetime.strptime(string, "%d.%m.%y").strftime("%a")
        wdays.append(day)


convert_date(date)
# convert_time(time)

print("There are {} words in your chat.".format(len(text)))
# print("There are {} emojis in your chat.".format(len(specials)))
print("Generating Wordcloud & Charts. Please wait…")

# sort dates & times + create dictionaries

d_obj = []
d_perf = []
d_count = {}


def sort_days(dataset, nameofday):
    for day in dataset:
        if day.startswith(nameofday):
            d_count.setdefault(day, 0)
            d_count[day] = d_count[day] + 1


sort_days(wdays, "Mon")
sort_days(wdays, "Tue")
sort_days(wdays, "Wed")
sort_days(wdays, "Thu")
sort_days(wdays, "Fri")
sort_days(wdays, "Sat")
sort_days(wdays, "Sun")


for k in d_count.keys():
    d_obj.append(k)

for n in d_count.values():
    d_perf.append(n)


t_sort = []
t_obj = []
t_perf = []
t_count = {}

clock.sort()

for t in clock:
    t_count.setdefault(t, 0)
    t_count[t] = t_count[t] + 1

t_key = t_count.keys()
t_val = t_count.values()

t_time = []

for item in t_key:  # convert time strings to datetime format
    item = datetime.datetime.strptime(item, "%H:%M").time()
    t_time.append(item)


# Generate & save weekdays bar chart

y_pos = np.arange(len(d_count))

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

xlabel("")
ylabel("# of messages")
title("Busiest times:")
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

# wordcloud mask from file
wa_mask = np.array(Image.open("wa_icon.png"))

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


# merge pictures

# merge_image takes three parameters first two parameters specify
# the two images to be merged and third parameter i.e. vertically
# is a boolean type which if True merges images vertically
# and finally saves and returns the file_name


def merge_image(img1, img2, vertically):
    images = list(map(Image.open, [img1, img2]))
    widths, heights = zip(*(i.size for i in images))
    if vertically:
        max_width = max(widths)
        total_height = sum(heights)
        new_im = Image.new('RGB', (max_width, total_height))

        y_offset = 0
        for im in images:
            new_im.paste(im, (0, y_offset))
            y_offset += im.size[1]
    else:
        total_width = sum(widths)
        max_height = max(heights)
        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]

    new_im.save('stats.png')
    return 'stats.png'


merge_image("days.png", "times.png", vertically=True)
merge_image("wc.png", "stats.png", vertically=False)


os.remove("days.png")
os.remove("times.png")

os.remove("wc.png")

# add current date
image = Image.open("stats.png")
font_type = ImageFont.truetype("Roboto_Black.ttf", 20)
draw = ImageDraw.Draw(image)
current_date = date[-1]
draw.text(xy=(70, 70), text=("Most frequent words & stats as of: " +
                             current_date), fill=(0, 0, 0), font=font_type)
image.save("final.png")

os.remove("stats.png")
