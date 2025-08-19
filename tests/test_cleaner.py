import unittest
from cleaner.cleaner import EthiopianTextCleaner

class TestEthiopianTextCleaner(unittest.TestCase):

    def setUp(self):
        self.cleaner = EthiopianTextCleaner()

    def test_clean_text(self):
        raw_text = "ሰላም።  Hello!!  "
        expected = "ሰላም hello"
        self.assertEqual(self.cleaner.clean_text(raw_text), expected)

if __name__ == "__main__":
    unittest.main()
