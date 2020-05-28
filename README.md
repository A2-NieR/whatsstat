<div align="center">
  <br>

![Logo](data/readme/256.png)
<br>

# WhatsStat

<br>

**A Python application that analyzes your exported WhatsApp chats using Qt for the GUI**
<br><br>
![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
<br><br>
[Features](README.md#Features) •
[Preparations](README.md#Preparations) •
[Usage](README.md#Usage)
<br>

</div>

## Features

<br>The application takes the exported .txt chat-file as input _(currently only English/German supported)_. <br>
The messages then get analyzed, prepared and the application finally generates an image containing:
<br>

- A wordcloud with the 500 most used words
- A bar chart showing the total number of messages during each day of the week
- A line chart showing the busiest times in a 24h timespan

<br>
<div align="center">

![Sample Output](data/readme/sample_output.png)

_Sample output with the default wordcloud form_

</div>
<br>

<br>

### Use a custom image for the generated wordcloud

Custom pictures can be selected to act as a mask for the resulting wordcloud. <br>
The picture has to be square with a white background:
<br><br>

<div align="center">

![Custom Wordcloud](data/readme/cstm_ani.gif)

_Custom picture with resulting wordcloud_

</div>
<br>

### Exclude common words like _"You, I, and… etc."_

Common words like articles and connectives can be excluded from the wordcloud:
<br><br>

<div align="center">

![Exclude common words](data/readme/wc_sws.gif)

_Common words included/excluded_

</div>
<br>

## Preparations

First you need to export a chat history using WhatsApp's _Export chat_ feature:
<br>

<div align="center">

![WhatsApp export](data/readme/wa_export.gif)

_Exporting a WhatsApp chat (Android)_

</div>
<br>
This will generate a .txt file containing the chat history. Copy this file anywhere
on your computer and select it in the WhatsStat application.

<br>

## Usage

1. Download the repository
2. Make sure the requirements are met on your machine
3. Navigate to **src/main/python** and run `$ python main.py`
