from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, subjectivity
from nltk.probability import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.classify import NaiveBayesClassifier
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import re

#DataFrame for customer contacts and pull out Verbatim, StopWords, and Stemmer
df = pd.read_csv(r"Contacts.csv")
calls = df['Verbatim']
stopWords = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

#Pulls sentences out for words
def tokenize_sentence(calls):
    sentenceFiltered = []
    for call in calls:
        sentence = sent_tokenize(call)
        for s in sentence:
            sentenceFiltered.append(s)
    print("SENTENCES FILTERED HERE: ")
    print(sentenceFiltered)
    tokenize_words(sentenceFiltered)

#Pulls words, stems and tokenizes
def tokenize_words(sentences):
    wordsFiltered = []
    for s in sentences:
        words = word_tokenize(s)
        print(words)
        for w in words:
            if w not in stopWords:
                wordsFiltered.append(lemmatizer.lemmatize(w))
    print("WORDS FILTERED HERE: ") 
    print(wordsFiltered)
    preprocess(wordsFiltered)    

#Process text, removing 
def preprocess(text):
    clean_words = []
    word_count = 0
    for x in text:
        new_text = re.sub('<.,&', '', x)
        new_text = re.sub(r'[^\w\s]','', new_text)
        new_text = re.sub(r'\d+', '', new_text)
        new_text = new_text.lower()
        if new_text != '' and new_text != 'customer':
            clean_words.append(new_text)
            word_count += 1
    print("NEW TEXT HERE: ")
    print(clean_words)
    print("Word Count is: " + str(word_count))
    fdist = FreqDist(clean_words)
    wordcloud = WordCloud(font_path='arial',scale= 3, background_color='white',max_words=100, max_font_size=20).generate(str(clean_words))
    plt.figure(figsize=(10,10))
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.show()

    return clean_words



# def tokenization_s(sentence):
#     s_new = []
#     for sent in sentence:
#         s_token = sent_tokenize(sent)
#         if s_token != '':
#             s_new.append(s_token)
#     print(s_new)
#     return s_new



# def tokenization_w(words):
#     w_new = []
#     for w in (words[:][0]):
#         w_token = word_tokenize(w)
#         if w_token != '':
#             w_new.append(w_token)
#     print(w_token)
#     return w_token


tokenize_sentence(calls)