import bs4 as bs
import urllib.request as urlr
import nltk
import string
import lxml
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec
nltk.download('punkt')
nltk.download('stopwords')

scrapped_data = urlr.urlopen('https://en.wikipedia.org/wiki/Machine_learning')
article = scrapped_data.read()
parsed_article = bs.BeautifulSoup(article, 'lxml')
paragraphs = parsed_article.find_all('p')
article_text = ""
for p in paragraphs:
    article_text += p.text

#print(article_text)

processed_article = article_text.lower()
processed_article = re.sub(r'\s+', ' ', processed_article)
processed_article = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]','', processed_article)
all_sentences = sent_tokenize(processed_article)
all_words = [word_tokenize(sent) for sent in all_sentences]
stops = set(stopwords.words('english'))
for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stops]

# for word in all_words:
#     for w in word:
#         print(w)
word2vec = Word2Vec(all_words, min_count=2)
vocabulary = word2vec.wv.key_to_index

print(*word2vec.wv.most_similar('machine'))
