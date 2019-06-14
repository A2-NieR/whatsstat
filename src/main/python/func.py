import re
import regex
import emoji
import datetime as dt
from PIL import Image


# store lines with messages only in separate list
def extract_nodate(database):
    chat_with_date = []
    chat_without_date = []
    for row in database:
        if len(row) == 1:
            chat_without_date.append(row)
        else:
            chat_with_date.append(row)
    return chat_without_date, chat_with_date


# remove "., .., ..." from message only list + store in new list
def clean_nodate(dataset):
    msg_only = []
    for row in dataset:
        for i in row:
            if i.startswith("."):
                continue
            else:
                msg_only.append(row)
    return msg_only


# store items in separate lists & remove names
def pull(dataset):
    date = []
    clock = []
    msg = []
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
    return date, clock, msg


# extract msg_only words into list
def open_list(dataset):
    msg_open = []
    for row in dataset:
        row = row[0]
        msg_open.append(row)
    return msg_open


# pull emojis in separate list
def extract_emojis(database):
    ems = []
    for row in database:
        text = regex.findall(r'\X', row)
        for word in text:
            if any(char in emoji.UNICODE_EMOJI for char in word):
                ems.append(word)
    return ems


# remove emojis, numbers, special characters & strip whitespace
def remove_nonletters(dataset):
    msgs_final = []
    junk = ("http", "Medien ausgeschlossen", "Die Sicherheitsnummer", "Sicherheitsnummer von", "ausgeschlossen Medien",
            "Nachrichten", "diese Nachricht", "Messages you send", "Media omitted", "omitted Media")
    for row in dataset:
        regex = re.compile('[^a-zA-ZäöüÄÖÜß]')
        words = (regex.sub(' ', row))
        words = words.strip()
        # remove empty items, urls & (security code) notification messages
        if words == "" or words.startswith(junk) or "security code" in words:
            continue
        else:
            msgs_final.append(words)
    return msgs_final


# Captain Caps to the rescue! Make everything WAMBO!
def caps(dataset):
    cpt_caps = []
    for item in dataset:
        cap = item.upper()
        cpt_caps.append(cap)
    return cpt_caps


# pull every word into separate list
def singled(dataset):
    single_words = []
    for item in dataset:
        item = item.split()
        for i in item:
            # remove single letters
            if len(i) == 1:
                continue
            else:
                single_words.append(i)
    return single_words


# convert dates into weekdays
def convert_date(dataset):
    wdays = []
    for string in dataset:
        try:
            day = dt.datetime.strptime(string, "%d.%m.%y").strftime("%a")
        except:
            day = dt.datetime.strptime(string, "%m/%d/%y").strftime("%a")
        wdays.append(day)
    return wdays


# create weekdays dictionary
def sort_days(dataset, week):
    d_count = {}
    for nameofday in week:
        for day in dataset:
            if day.startswith(nameofday):
                d_count.setdefault(day, 0)
                d_count[day] = d_count[day] + 1
    return d_count


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


def resize_image(img):
    original_image = Image.open(img)
    size = (1920, 1920)
    resized_image = original_image.resize(size)
    resized_image.save("resize.png")
