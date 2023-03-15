import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import defaultdict
nltk.download('punkt')
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('omw-1.4')
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
from nltk.metrics.distance import edit_distance

#Reading corpus
def read_file(file_name): #function to read files
  with open('/content/drive/MyDrive/Corpus/{}'.format(file_name)) as f:
    text = str(f.read())
  return text
lines = read_file("doc_1.txt")

#removing punctuation
def rem_punctuation(lines):
    text  = "".join([char for char in lines if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text

#preprocessing text ( Case folding, normalization, tokenization, stop word removal, lemmatization/stemming)
def preprocess_text(lines):
    text = rem_punctuation(lines)
    text = text.lower() # case folding
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text) # normalization
    tokens = word_tokenize(text) # tokenization
    tokens = [token for token in tokens if token not in stop_words] # stop word removal
    tokens = [lemmatizer.lemmatize(token) for token in tokens] # lemmatization/stemming
    return tokens

#building inverted index
def build_inverted_index(documents):
    inverted_index = {}
    for doc_id, doc in enumerate(documents):
        tokens = preprocess_text(doc)
        for token in set(tokens):
            if token not in inverted_index:
                inverted_index[token] = []
            inverted_index[token].append(doc_id)
    return inverted_index

#search function
def search(inverted_index, query):
    query_tokens = preprocess_text(query)
    query_stack = []
    for token in query_tokens:
        if token in inverted_index:
            query_stack.append(set(inverted_index[token]))
        else:
            query_stack.append(set())
    result = set.intersection(*query_stack) if 'AND' in query else set.union(*query_stack)
    return result
