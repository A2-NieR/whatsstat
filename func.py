import re
import regex
import emoji
import datetime
from PIL import Image


# store lines with messages only in separate list
chat_with_date = []
chat_without_date = []


def extract_nodate(database):
    for row in database:
        if len(row) == 1:
            chat_without_date.append(row)
        else:
            chat_with_date.append(row)


# remove "., .., ..." from message only list + store in new list
msg_only = []


def clean_nodate(dataset):
    for row in dataset:
        # row = list(row)
        for i in row:
            if i.startswith("."):
                continue
            else:
                msg_only.append(row)


# store items in separate lists & remove names
date = []
clock = []
msg = []


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


# extract msg_only words into list
msg_open = []


def open_list(dataset):
    for row in dataset:
        row = row[0]
        msg_open.append(row)


# pull emojis in separate list
ems = []


def extract_emojis(database):
    for row in database:
        text = regex.findall(r'\X', row)
        for word in text:
            if any(char in emoji.UNICODE_EMOJI for char in word):
                ems.append(word)


# remove emojis, numbers, special characters & strip whitespace
messages_final = []


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


# Captain Caps to the rescue! Make everything WAMBO!
cpt_caps = []


def caps(dataset):
    for item in dataset:
        cap = item.upper()
        cpt_caps.append(cap)


# pull every word into separate list
single_words = []


def singled(dataset):
    for item in dataset:
        item = item.split()
        for i in item:
            # remove single letters
            if len(i) == 1:
                continue
            else:
                single_words.append(i)


# convert dates into weekdays
wdays = []


def convert_date(dataset):
    for string in dataset:
        day = datetime.datetime.strptime(string, "%d.%m.%y").strftime("%a")
        wdays.append(day)


# create weekdays dictionary
d_count = {}


def sort_days(dataset, nameofday):
    for day in dataset:
        if day.startswith(nameofday):
            d_count.setdefault(day, 0)
            d_count[day] = d_count[day] + 1


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
