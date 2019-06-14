import unittest
import re
import regex
import emoji
import datetime as dt
import sys
sys.path.append('../src/main/python')
import func


class TestFunc(unittest.TestCase):

    """@classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown\n")"""

    def test_extract_nodate(self):
        msg = [['03.12.17', '22:26 - Michael: Hello'], ['Line without date'], ['03.12.17', "22:28 - Alex: What's up?"], ["Line2 without date"]]
        self.assertEqual(func.extract_nodate(msg), ([['Line without date'], ["Line2 without date"]], [['03.12.17', '22:26 - Michael: Hello'], ['03.12.17', "22:28 - Alex: What's up?"]]))

    def test_clean_nodate(self):
        msg = [['Hello'], ["."], ["What's up?"], ["..."], [".."]]
        self.assertEqual(func.clean_nodate(msg), [['Hello'], ["What's up?"]])

    # BUG Function working, test not working
    def test_pull(self):
        msg = [['03.12.17', '22:26 - Michael: Hello'], ['03.12.17', '22:28 - Alex: Hi there']]
        self.assertEqual(func.pull(msg), (['03.12.17', '03.12.17'], ['22:26', '22:28'], ['Hello', 'Hi there']))

    def test_open_list(self):
        msg = [["Line without date"], ["Line2 without date"]]
        self.assertEqual(func.open_list(msg), ["Line without date", "Line2 without date"])

    """def test_extract_emojis(self):
        pass"""

    def test_remove_nonletters(self):
        msg = ["http", "Medien ausgeschlossen", "Die Sicherheitsnummer", "Sicherheitsnummer von", "ausgeschlossen Medien", "Nachrichten, die", "diese Nachricht", "Messages you send", "Media omitted", "omitted Media", "security code", "Line without date", "Line2 without date"]
        self.assertEqual(func.remove_nonletters(msg), ["Line without date", "Line  without date"])

    def test_caps(self):
        msg = ["Line without date", "Line  without date"]
        self.assertEqual(func.caps(msg), ["LINE WITHOUT DATE", "LINE  WITHOUT DATE"])

    def test_singled(self):
        msg = ["LINE WITHOUT DATE", "LINE  WITHOUT DATE"]
        self.assertEqual(func.singled(msg), ["LINE", "WITHOUT", "DATE", "LINE", "WITHOUT", "DATE"])

    def test_convert_date(self):
        dat = ['03.12.17', '03.01.19']
        self.assertEqual(func.convert_date(dat), ["Sun", "Thu"])

    def test_sort_days(self):
        week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        days = ["Sun", "Thu", "Mon", "Thu"]
        self.assertEqual(func.sort_days(days, week), {"Mon": 1, "Thu": 2, "Sun": 1})


if __name__ == "__main__":
    unittest.main()
