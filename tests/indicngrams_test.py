#! /usr/bin/python
#run python -m chardetails.tests.chardetails_test from root directory
#of the repository
import unittest
from indicngram import getInstance


class TestIndicNgram(unittest.TestCase):

    def setUp(self):
        self.instance = getInstance()

    def test_info(self):
        self.assertEqual('Ngram Library for English and Indian languages',
                         self.instance.get_info())

    def test_letterNgram_English(self):
        self.assertEqual(self.instance.letterNgram("catterpillar"),
                            ['ca', 'at', 'tt', 'te', 'er', 'rp',
                            'pi', 'il', 'll', 'la', 'ar'])

    def test_wordNgram_English(self):
        self.assertEqual(self.instance.wordNgram("The quick brown fox jumped over the lazy dog"),  [['The', 'quick'],
                                                         ['quick', 'brown'],
              ['brown', 'fox'],
               ['fox', 'jumped'],
                ['jumped', 'over'],
                 ['over', 'the'],
                  ['the', 'lazy'],
                   ['lazy', 'dog']])

    def test_syllableNgram_English(self):
        self.assertEqual(self.instance.syllableNgram("catterpillar",4),[' cat',
 'cat-',
 'at-t',
 't-te',
 '-ter',
 'ter-',
 'er-p',
 'r-pi',
 '-pil',
 'pil-',
 'il-l',
 'l-la',
 '-lar',
 'lar '] )


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIndicNgram)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
