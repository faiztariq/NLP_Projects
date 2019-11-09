# This is a demo for nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = "Pizza is bad"

sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sentence)
print(ss)