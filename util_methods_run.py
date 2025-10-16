import unittest

class TestStrings(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("spam".upper(), "SPAM")

if __name__ == "__main__":
    from util_methods import *
    print(convert_hex_bin("5f"))
    import doctest
    print(help("modules"))
    print(doctest.testmod(verbose=True))