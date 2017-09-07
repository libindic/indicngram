# LibIndic N-gram Generator
[![Build Status](https://travis-ci.org/libindic/indicngram.svg?branch=master)](https://travis-ci.org/libindic/indicngram)
[![Coverage Status](https://coveralls.io/repos/github/libindic/indicngram/badge.svg?branch=master)](https://coveralls.io/github/libindic/indicngram?branch=master)

An n-gram generator for indic languages.

## What is Ngram?

An n-gram model is a type of probabilistic model for predicting the
next item in a sequence.  n-grams are used in various areas of
statistical natural language processing and genetic sequence analysis.

An n-gram is a subsequence of n items from a given sequence.  The
items in question can be phonemes, syllables, letters, words or base
pairs according to the application. 

An n-gram of size 1 is referred to as a "unigram"; size 2 is a
"bigram" (or, less commonly, a "digram"); size 3 is a "trigram"; and
size 4 or more is simply called an "n-gram".


## Installation
1. Clone the repository `git clone https://github.com/libindic/indicngram.git`
2. Change to the cloned directory `cd indicngram`
3. Run setup.py to create installable source `python setup.py sdist`
4. Install using pip `pip install dist/libindic-ngram*.tar.gz`

## Usage
```
Input Parameters: Text and value of N (default value 2)
Output: List of grams


>>> from libindic.ngram import Ngram
>>> ngram_generator = Ngram()
>>> ngram_gerator(<text>, <window size>)
```

##### Example
```
>>> from libindic.ngram import Ngram
>>> ngram_generator = Ngram()
>>> text = "Languages"
>>> grams = ngram_generator.letterNgram(text, 3)
>>> print(grams)
['Lan', 'ang', 'ngu', 'gua', 'uag', 'age', 'ges']
>>> for gram in grams:
...     print("".join(gram))

Lan
ang
ngu
gua
uag
age
ges
```
## Tests
Run tests with ``python setup.py test``

Read the [docs](http://indicngram.rtfd.org) for more.
