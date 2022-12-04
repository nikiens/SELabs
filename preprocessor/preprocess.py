import spacy

def tokenize(text):
	out = []
	nlp = spacy.load("en_core_web_sm")

	for token in nlp(text):
		out.append(token.text)

	return out