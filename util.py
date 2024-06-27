import nltk
# nltk.download('punkt')
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("english")

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    pass

# a = "How do I download the application"
# print(a)
# a = tokenize(a)
# print(a)

words = ["connects", "connected", "connecting"]
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)

