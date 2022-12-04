import spacy
import nltk

from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer

def tokenize(text):
	out = []
	nlp = spacy.load("en_core_web_sm")

	for token in nlp(text):
		out.append(token.text)

	return out

def lowercase(text):
	return text.lower().split()

def stem(doc):
	out = []
	stemmer = PorterStemmer()

	for token in doc:
		out.append(stemmer.stem(token))

	return out

def lemmatize(doc):
	out = []
	lemmatizer = WordNetLemmatizer()

	for token in doc:
		out.append(lemmatizer.lemmatize(token))

	return out