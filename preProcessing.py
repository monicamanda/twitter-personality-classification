import re
import nltk
import pandas as pd


def casefolding(review):
    review = review.lower()
    return review


def tokenize(review):
    token = nltk.word_tokenize(review)
    return token


def filtering(review):
    # Remove angka termasuk angka yang berada dalam string
    # Remove non ASCII chars
    review = re.sub(r'[^\x00-\x7f]', r'', review)
    review = re.sub(r'(\\u[0-9A-Fa-f]+)', r'', review)
    review = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", review)
    review = re.sub(r'\\u\w\w\w\w', '', review)
    # Remove link web
    review = re.sub(r'http\S+', '', review)
    # Remove @username
    review = re.sub(r'@[^\s]+', '', review)
    # Remove #tagger
    review = re.sub(r'#([^\s]+)', '', review)
    # Remove simbol, angka dan karakter aneh
    review = re.sub(r"[.,:;+!\-_<^/=?\"'\(\)\d\*]", " ", review)
    return review


def replaceThreeOrMore(review):
    # Pattern to look for three or more repetitions of any character,
    # including newlines (contoh goool -> gol).
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1", review)


def convertToSlangword(review):
    # Membuka dictionary slangword
    kamus_slangword = eval(open("slangwords.txt").read())
    # Search pola kata (contoh kpn -> kapan)
    pattern = re.compile(r'\b( ' + '|'.join(kamus_slangword.keys())+r')\b')
    content = []
    for kata in review:
        # Replace slangword berdasarkan pola review yg telah ditentukan
        filteredSlang = pattern.sub(lambda x: kamus_slangword[x.group()], kata)
        content.append(filteredSlang.lower())
    review = content
    return review


def removeStopword(review):
    stopwords = open('stopword-tala.txt', 'r').read().split()
    content = []
    filteredtext = [word for word in review.split() if word not in stopwords]
    content.append(" ".join(filteredtext))
    review = content
    return review


def byteParser(review):
    reviews = []
    i = 0
    for target in review.values:
        for words in target:
            arrayWords = words.split('"')
            if len(arrayWords) > 1:
                reviews.append(arrayWords[1])
                i += 1
            else:
                arrayWords = words.split("'")
                reviews.append(arrayWords[1])
                i += 1
    print('total:', i)
    return reviews


data_tweets = pd.read_csv('tweets-@_monicamanda.csv', usecols=[
                          2], skiprows=1, header=None, index_col=False,
                          encoding='latin-1')

data = byteParser(data_tweets)
for tweet in data:
    tweet = casefolding(tweet)
    print(tweet)
