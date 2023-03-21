import glob
import string

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer, word_tokenize
import pandas as pd

def create_dic(path):
  dic = {}
  files = glob.glob(path)
  for file in files:
      name = file.split('/')[-1] #it file.split is the entire file path and -1 retrieves the file name
      with open(file, 'r') as f:
          text = f.read()
      dic[name] = text
  return dic

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
sp = punc.split()
def normalized_wordlist(dic):
    stop = stopwords.words('english') + sp + ['\n']
    word_list = []
    for doc in dic.values():
        for word in word_tokenize(doc.lower().strip()):
            if not word in stop and len(word) != 1:
                word_list.append(word)



    return word_list

#def password_check():

    if password in word_list:

        return "YOUR PASSWORD HAS BEEN LEAKED"





if __name__  == "__main__":
    path = 'Database/*.txt'

    disc = create_dic(path)
    n_word = normalized_wordlist(disc)
    print(n_word)
