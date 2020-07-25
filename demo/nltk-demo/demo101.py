# This is a demo for nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# sentence = "Pizza is bad"

# sid = SentimentIntensityAnalyzer()
# ss = sid.polarity_scores(sentence)
# print(ss)

from nltk import tokenize

sentences = ["Python is awesome.", "NLTK rocks big time."]
paragraph = "This is my first NLTK tutorial. It's super cool and I love it!"
tricky_sentences = ["Python's AMAZING!!!", "NLTK, Hell YAY!"]

lines_list = tokenize.sent_tokenize(paragraph)

sentences.extend(lines_list)

sentences.extend(tricky_sentences)

sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()