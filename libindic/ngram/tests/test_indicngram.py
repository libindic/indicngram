#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Ngram


class IndicNgramTest(TestCase):

    def setUp(self):
        super(IndicNgramTest, self).setUp()
        self.ngram = Ngram()

    def test_letterNgram_English(self):
        self.assertEqual(self.ngram.letterNgram("catterpillar"),
                         ['ca', 'at', 'tt', 'te', 'er', 'rp',
                          'pi', 'il', 'll', 'la', 'ar'])

    def test_wordNgram_English(self):
        self.assertEqual(self.ngram.wordNgram("The quick \
        brown fox jumped over the lazy dog"),
                         [['The', 'quick'],
                          ['quick', 'brown'],
                          ['brown', 'fox'],
                          ['fox', 'jumped'],
                          ['jumped', 'over'],
                          ['over', 'the'],
                          ['the', 'lazy'],
                          ['lazy', 'dog']])

    def test_syllableNgram_English(self):
        self.assertEqual(self.ngram.syllableNgram("catterpillar", 4),
                         [' cat', 'cat-', 'at-t', 't-te', '-ter', 'ter-',
                          'er-p', 'r-pi', '-pil', 'pil-', 'il-l', 'l-la',
                          '-lar', 'lar '])

    def test_syllableNgram_Malayalam(self):
        self.assertEqual(self.ngram.syllableNgram(u"അധ്യാപകൻ"),
                         [[u'അ', u'ധ്യാ'],
                          [u'ധ്യാ', u'പ'],
                          [u'പ', u'ക'],
                          [u'ക', u'ൻ']])
