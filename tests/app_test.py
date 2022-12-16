import unittest
import sys
import os

sys.path.append(os.path.abspath("../preprocessor/"))

from preprocess import *

class TestMethods(unittest.TestCase):

	def test_tokenize(self):
		self.assertEqual(['hello', 'world'], tokenize('hello world'))

	def test_lowercase(self):
		self.assertEqual(['hello', 'world'], lowercase('HeLLo WoRld'))

	def test_stem(self):
		self.assertEqual(['autocomplet'], stem(['autocomplete']))

	def test_remove_stopwords(self):
		self.assertEqual([], remove_stopwords(['is']))

if __name__ == '__main__':
	unittest.main()