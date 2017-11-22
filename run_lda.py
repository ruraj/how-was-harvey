import csv

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora

n_topics = 3

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
  stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
  punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
  normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
  return normalized

with open('Hurricane_Harvey_full_utf8.csv') as csvfile:
  twitter_data = csv.reader(csvfile, delimiter=',', quotechar='"')

  # Let's remove all punctuations and special characters (only words)
  tweets = [clean(tweet[6]).split() for tweet in twitter_data]

  ####### LDA
  # Let's make a dictionary
  dictionary = corpora.Dictionary(tweets)
  
  # Let's convert the dictionary to a document term matrix
  term_matrix = [dictionary.doc2bow(tweet) for tweet in tweets]
  
  # Time to run the LDA!
  lda_model = gensim.models.ldamodel.LdaModel(term_matrix, num_topics=n_topics, id2word=dictionary, passes=10)

  # Show a fancy wordcloud
  import matplotlib
  matplotlib.use('Agg') # To run headless
  import matplotlib.pyplot as plt
  from wordcloud import WordCloud
  
  for t in range(n_topics):
    plt.figure()
    words = dict(lda_model.show_topic(t))
    print(words)
    plt.imshow(WordCloud().fit_words(words))
    plt.axis("off")
    plt.savefig('topic' + str(t) + '.png')

  print(lda_model.print_topics())

