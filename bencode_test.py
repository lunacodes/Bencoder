import unittest
from bencode2 import * 

class BencodeTest(unittest.TestCase):
    def test_str_length(self):
        self.assertEqual(ben_str("spam"), "4:spam")

    def test_ben_int(self):
        self.assertEqual(ben_int(43), "i43e")

    def test_bin_list(self):
        self.assertEqual(ben_list(["luna", "friend"]), "l4:luna6:friende")

    def test_bin_dict(self):
        self.assertEqual(ben_dict({"cow":"moo", "spam":"eggs"}), "d3:cow3:moo4:spam4:eggse")

class DecodeTest(unittest.TestCase):
    def test_decode_str(self):
        self.assertEqual(dec_str("4:spam"), "spam")
    def test_decode_int(self):
        self.assertEqual(dec_int("i43e"), 43)
    def test_decode_list(self):
        self.assertEqual(dec_list("l4:luna6:friende"), ["luna", "friend"])
    def test_decode_dict(self):
        self.assertEqual(dec_dict("d3:cow3:moo4:spam4:eggse"), {"cow":"moo", "spam":"eggs"} )


if __name__ == "__main__":
    unittest.main()