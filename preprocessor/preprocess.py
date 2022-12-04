import spacy
import nltk

from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

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

def remove_stopwords(doc):
	out = []

	stop_words = set(stopwords.words("english"))

	for token in doc:
		 if token not in stop_words:
		 	out.append(token)

	return out

if __name__ == "__main__":
	st.title("Basic text preprocessor for NLP tasks")

	message = st.text_area("Enter text", "Type here")
	if st.checkbox("Tokenize"):
		result = tokenize(message)
		st.success(result)

	if st.checkbox("Lowercase"):
		result = lowercase(message)
		st.success(result)

	if st.checkbox("Stem"):
		result = stem(tokenize(message))
		st.success(result)

	if st.checkbox("Lemmatize"):
		result = lemmatize(tokenize(message))
		st.success(result)

	if st.checkbox("Remove stopwords"):
		result = remove_stopwords(tokenize(message))
		st.success(result)

	st.sidebar.subheader("Software Engineering Lab 2")
	st.sidebar.markdown(
		"""
		#### Supported features:
		+ Tokenization
		+ Lowercase convert
		+ Stemming
		+ Lemmatization
		+ Stop words cleaning
		"""
	)

