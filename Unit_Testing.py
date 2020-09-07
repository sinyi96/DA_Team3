import unittest
import os

class TestMyProgram(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\heng_\\PycharmProjects\\DA_Team3\\recon.py")
        os.system("C:\\Users\\heng_\\PycharmProjects\\DA_Team3\\webcrawling.py")
        os.system("C:\\Users\\heng_\\PycharmProjects\\DA_Team3\\Imagelinks.py")

    if __name__ == "__main__":
        unittest.main()