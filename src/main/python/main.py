# Generated main ui code from "puic5 -x uiFile.ui -o uiFile.py"
# libraries for UI
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import jtextfsm as textfsm
from fbs_runtime.application_context import ApplicationContext

# standard + custom libraries
import os
import datetime as dt
from csv import reader
import ntpath
import func

# libraries for graphs & wordcloud
import numpy as np
import pylab as pl
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
plt.rcdefaults()


# class for console outputs in QTextEdit
class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


# main ui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/base/32.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        """self.exp_size = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exp_size.sizePolicy().hasHeightForWidth())
        self.exp_size.setSizePolicy(sizePolicy)
        self.exp_size.setObjectName("exp_size")
        self.exp_size.addItem("")
        self.exp_size.addItem("")
        self.gridLayout.addWidget(self.exp_size, 3, 1, 1, 3)"""
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.select_txt = QtWidgets.QLabel(self.centralwidget)
        self.select_txt.setObjectName("select_txt")
        self.gridLayout.addWidget(self.select_txt, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setObjectName("generate")
        self.horizontalLayout.addWidget(self.generate)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 4)
        # self.save_to = QtWidgets.QToolButton(self.centralwidget)
        # self.save_to.setObjectName("save_to")
        # self.gridLayout.addWidget(self.save_to, 5, 3, 1, 1)
        self.open_img = QtWidgets.QToolButton(self.centralwidget)
        self.open_img.setObjectName("open_img")
        self.gridLayout.addWidget(self.open_img, 1, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.display = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setItalic(True)
        self.display.setFont(font)
        self.display.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.display.setObjectName("display")
        self.horizontalLayout_2.addWidget(self.display)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 4)
        self.no = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no.sizePolicy().hasHeightForWidth())
        self.no.setSizePolicy(sizePolicy)
        self.no.setObjectName("no")
        self.gridLayout.addWidget(self.no, 2, 3, 1, 1)
        # self.select_save = QtWidgets.QLabel(self.centralwidget)
        # self.select_save.setObjectName("select_save")
        # self.gridLayout.addWidget(self.select_save, 5, 0, 1, 1)
        """self.select_size = QtWidgets.QLabel(self.centralwidget)
        self.select_size.setObjectName("select_size")
        self.gridLayout.addWidget(self.select_size, 3, 0, 1, 1)"""
        self.select_img = QtWidgets.QLabel(self.centralwidget)
        self.select_img.setObjectName("select_img")
        self.gridLayout.addWidget(self.select_img, 1, 0, 1, 1)
        self.excl_stopw = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.excl_stopw.sizePolicy().hasHeightForWidth())
        self.excl_stopw.setSizePolicy(sizePolicy)
        self.excl_stopw.setObjectName("excl_stopw")
        self.gridLayout.addWidget(self.excl_stopw, 2, 0, 1, 1)
        self.yes = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yes.sizePolicy().hasHeightForWidth())
        self.yes.setSizePolicy(sizePolicy)
        self.yes.setObjectName("yes")
        self.gridLayout.addWidget(self.yes, 2, 2, 1, 1)
        self.open_txt = QtWidgets.QToolButton(self.centralwidget)
        self.open_txt.setObjectName("open_txt")
        self.gridLayout.addWidget(self.open_txt, 0, 3, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # get sys.stdout to print in gui
        sys.stdout = Stream(newText=self.onUpdateText)


# Ui connections calling functions defined below
        # BUG if no file is selected + cancel button => program crashes
        self.open_txt.clicked.connect(self.setChat)
        self.open_img.clicked.connect(self.setImage)

        self.yes.clicked.connect(self.stopW)
        self.no.clicked.connect(self.noStopW)

        # self.save_to.clicked.connect(self.saveFile)

        self.generate.clicked.connect(self.genFile)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "WhatsStat – Chat Analyzer"))
        # self.exp_size.setItemText(0, _translate("MainWindow", "3200 x 1920 px"))
        # self.exp_size.setItemText(1, _translate("MainWindow", "1600 x 960 px"))
        self.select_txt.setText(_translate(
            "MainWindow", "Select exported chat .txt file:"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        # self.save_to.setText(_translate("MainWindow", "..."))
        self.open_img.setText(_translate("MainWindow", "..."))
        self.no.setText(_translate("MainWindow", "No"))
        # self.select_save.setText(_translate(
        #    "MainWindow", "Choose save location:"))
        # self.select_size.setText(_translate("MainWindow", "Choose size for results:"))
        self.select_img.setText(_translate(
            "MainWindow", "Use custom picture (or leave blank for default)"))
        self.excl_stopw.setText(_translate(
            "MainWindow", "Exclude most common words? (I, You, and… etc.)"))
        self.yes.setText(_translate("MainWindow", "Yes"))
        self.open_txt.setText(_translate("MainWindow", "..."))

# Functions for ui interactions
    # output of console messages in QTextEdit box
    def onUpdateText(self, text):
        cursor = self.display.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.display.setTextCursor(cursor)
        self.display.ensureCursorVisible()

    def __del__(self):
        sys.stdout = sys.__stdout__

    # open chat textfile
    def setChat(self):
        # filter prevents from returning file as tuple
        txtName, _filter = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Chat", "", "Text files (*.txt)")

        if txtName:
            print(ntpath.basename(str(txtName)) + " successfully loaded.")
        # BUG When not choosing a file: FileNotFoundError: [Errno 2] No such file or directory: ''

        opened_file = open(txtName)
        read_file = reader((line.replace("\0", "") for line in opened_file))
        chat = list(read_file)
        chat_full = []

    # delete empty lines in text
        for row in chat:
            if row != []:
                chat_full.append(row)

        # chat_header = chat_full[0]
        chat_main = chat_full[1:]

        func.extract_nodate(chat_main)
        func.clean_nodate(func.chat_without_date)
        func.pull(func.chat_with_date)
        func.open_list(func.msg_only)

    # merge messages into one file
        msgs = func.msg + func.msg_open

        # TODO: Find a way to use the extracted emojis
        func.extract_emojis(msgs)
        func.remove_nonletters(msgs)

        func.caps(func.messages_final)
        func.singled(func.cpt_caps)

        self.text = " ".join(func.single_words)
        # self.special = " ".join(func.ems)
        # self.specials = special.encode('utf-8')

        func.convert_date(func.date)
        # convert self.t_time(time)

    # sort dates & times + create dictionaries
        func.sort_days(func.wdays, "Mon")
        func.sort_days(func.wdays, "Tue")
        func.sort_days(func.wdays, "Wed")
        func.sort_days(func.wdays, "Thu")
        func.sort_days(func.wdays, "Fri")
        func.sort_days(func.wdays, "Sat")
        func.sort_days(func.wdays, "Sun")

    # extract keys&values from weekdays dictionary
        self.d_obj = []
        self.d_perf = []

        for k in func.d_count.keys():
            self.d_obj.append(k)

        for n in func.d_count.values():
            self.d_perf.append(n)

    # extract keys&values from dictionary (from extracted times)
        t_count = {}

        func.clock.sort()

        for t in func.clock:
            t_count.setdefault(t, 0)
            t_count[t] = t_count[t] + 1

        t_key = t_count.keys()
        self.t_val = t_count.values()

    # convert time strings to datetime format
        self.t_time = []

        for item in t_key:
            item = dt.datetime.strptime(item, "%H:%M").time()
            self.t_time.append(item)

        self.signal = False

    # open custom image for wordcloud
    def setImage(self):
        self.imgName, _filter = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")

        # BUG When not choosing a file: AttributeError: 'str' object has no attribute 'read'

        # TODO if image is 1920x1920 don't resize
        """func.resize_image(self.imgName)
        self.resized = Image.open("resize.png")"""

        print(ntpath.basename(str(self.imgName)) + " successfully loaded.")

        self.signal = True

    # radio buttons for stopwords
    def stopW(self):
        self.stopwords = set(STOPWORDS)

        with open("../../../data/stopwords.txt") as osw:
            sw = [line.strip(",\n'") for line in osw]
            sw = [line.upper() for line in sw]
            sw = [line.split() for line in sw]

        stopw = []
        for sublist in sw:
            for item in sublist:
                stopw.append(item)

        self.stopwords.update(stopw)

        print("Stopwords selected.")

    def noStopW(self):
        self.no_stopwords = None

        print("No stopwords selected.")

    # TODO choose filesize
    """def sizing(self):
        if xyz == 3200:
            self.size = 200
        else:
            self.size = 100"""

    # TODO save file dialogue
    """def saveFile(self):
        # folder = QtWidgets.QFileDialog.setDirectory()
        self.saveName = QtWidgets.QFileDialog.getSaveFileName(
            None, "Save File", folder + "final.png", "Image Files (*.png *.jpg *.jpeg *.bmp)")"""

    # generate final image
    def genFile(self):

        self.progressBar.setValue(1)

        print("There are {} words in your chat.".format(len(self.text)))
        # print("There are {} emojis in your chat.".format(len(self.specials)))

    # Generate & save weekdays bar chart
        y_pos = np.arange(len(func.d_count))

        fig = plt.figure()
        plt.bar(y_pos, self.d_perf, align="center", alpha=0.5)
        plt.xticks(y_pos, self.d_obj)
        plt.ylabel('# of messages')
        plt.title('Busiest days:')
        fig.savefig("days.png", dpi=200)

        self.progressBar.setValue(25)

    # Generate & save time line chart
        fig = plt.figure()

        x = self.t_time
        y = self.t_val

        pl.xlabel("")
        pl.ylabel("# of messages")
        pl.title("Busiest times:")
        ax = plt.gca()
        # OPTIMIZE: set x-axis to 0-24h
        hours = [dt.time(0, 0), dt.time(1, 0), dt.time(2, 0), dt.time(3, 0),
                 dt.time(4, 0), dt.time(5, 0), dt.time(6, 0), dt.time(7, 0),
                 dt.time(8, 0), dt.time(9, 0), dt.time(10, 0), dt.time(11, 0),
                 dt.time(12, 0), dt.time(13, 0), dt.time(14, 0), dt.time(15, 0),
                 dt.time(16, 0), dt.time(17, 0), dt.time(18, 0), dt.time(19, 0),
                 dt.time(20, 0), dt.time(21, 0), dt.time(22, 0), dt.time(23, 0),
                 dt.time(23, 59)]

        ax.set_xticks(hours)
        plt.xticks(fontsize=7)
        plt.gcf().autofmt_xdate()
        plt.plot(x, y, linewidth=0.5)
        fig.savefig("times.png", dpi=200)

        print("…")

        self.progressBar.setValue(50)

        # TODO stopwords results
        if self.yes.isChecked():
            stop = self.stopwords
        elif self.no.isChecked():
            stop = self.no_stopwords

        if self.signal is True:
            # TODO if image is 1920x1920 don't resize
            func.resize_image(self.imgName)
            self.resized = Image.open("resize.png")
            # colored wordcloud with custom image
            color_mask = np.array(self.resized)

            # IDEA Maybe let user choose from a handful of fonts + max_words, fontsize, etc.
            wc = WordCloud(mask=color_mask, stopwords=stop, max_words=500, background_color='white',
                           font_path="../../../data/Roboto_Black.ttf")

            wc.generate(self.text)

            self.progressBar.setValue(60)

            # create coloring from image
            image_colors = ImageColorGenerator(color_mask)

            # display the generated image:
            fig, axes = plt.subplots(1, 3)
            axes[0].imshow(wc, interpolation="bilinear")

            # recolor wordcloud and show
            axes[1].imshow(wc.recolor(color_func=image_colors),
                           interpolation="bilinear")
            axes[2].imshow(color_mask, cmap=plt.cm.gray,
                           interpolation="bilinear")

            for ax in axes:
                ax.set_axis_off()

            # save final wordcloud
            # TODO: Let user choose save location
            wc.to_file("wc.png")

            os.remove("resize.png")

        else:
            print("Generating Wordcloud with default image.")
            # wordcloud mask from file
            wa_mask = np.array(Image.open("../../../data/wa_mask.png"))

            # Create and generate a wordcloud
            wordcloud = WordCloud(mask=wa_mask, stopwords=stop, max_words=500,
                                  background_color='white', font_path="../../../data/Roboto_Black.ttf")

            wordcloud.generate(self.text)

            self.progressBar.setValue(60)

            wordcloud.to_file("wc.png")

            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.figure()
            plt.imshow(wa_mask, cmap=plt.cm.gray, interpolation='bilinear')
            plt.axis("off")

        self.progressBar.setValue(70)

        func.merge_image("days.png", "times.png", vertically=True)
        func.merge_image("wc.png", "stats.png", vertically=False)

        os.remove("days.png")
        os.remove("times.png")

        os.remove("wc.png")

        self.progressBar.setValue(90)

    # add current date to top left on final image
        image = Image.open("stats.png")
        font_type = ImageFont.truetype("../../../data/Roboto_Black.ttf", 24)
        draw = ImageDraw.Draw(image)
        current_date = func.date[-1]
        draw.text(xy=(70, 70), text=("Most frequent words & stats as of: " +
                                     current_date), fill=(0, 0, 0), font=font_type)
        image.save("final.png")

        location = os.path.abspath("final.png")

        os.remove("stats.png")

        print("Done. Your final image is located here: " + location)

        self.progressBar.setValue(100)


if __name__ == "__main__":
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # sys.exit(app.exec_())
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
