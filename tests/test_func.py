import unittest
import ...sample/func


class testFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown\n")

    def test_dataset(self):
        pass


if __name__ == "__main__":
    unittest.main()
