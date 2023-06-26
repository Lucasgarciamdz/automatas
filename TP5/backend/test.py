import unittest
import re
from automatas.TP5.backend.csv_tool import DATE_RE, MAC_RE, USER_RE

class test_regex(unittest.TestCase):
    
    def test_date1(self):
        self.assertTrue(re.fullmatch(DATE_RE, "2019-12-31"))
    def test_date2(self):
        self.assertIsNone(re.fullmatch(DATE_RE, "2000-12-01"))
    def test_date3(self):
        self.assertIsNone(re.fullmatch(DATE_RE, "2020-13-01"))
    def test_date4(self):
        self.assertIsNone(re.fullmatch(DATE_RE, "2020-12-32"))
    def test_MAC(self):
        self.assertTrue(re.fullmatch(MAC_RE, "00:00:00:00:00:00"))
    def test_MAC2(self):
        self.assertTrue(re.fullmatch(MAC_RE, "00-00-00-00-00-00"))
    def test_MAC3(self):
        self.assertIsNone(re.fullmatch(MAC_RE, "0:00:00:00:0:00"))
    def test_MAC4(self):
        self.assertIsNone(re.fullmatch(MAC_RE, "00:00:00:00:00:000"))
    def test_MAC5(self):
        self.assertIsNone(re.fullmatch(MAC_RE, "\0:00:00:00:00:00"))
    def test_user1(self):
        self.assertTrue(re.fullmatch(USER_RE, "pepe"))
    def test_user2(self):
        self.assertTrue(re.fullmatch(USER_RE, "pEpE"))
    def test_user4(self):
        self.assertIsNone(re.fullmatch(USER_RE, "pepe-honguito"))
    def test_user5(self):
        self.assertIsNone(re.fullmatch(USER_RE, "pepe_honguito"))

if __name__ == "__main__":
    unittest.main()
