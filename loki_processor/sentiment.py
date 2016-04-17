# -*- coding: utf-8 -*-

""" sentiment.py

Basic Sentiment analyzer using NLTK and Pattern
(underneath the hood of TextBlob)
"""


# 3rd Party assets
from textblob import TextBlob


__author__ = 'Jared M Smith'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Jared M Smith'
__email__ = 'jared@jaredsmith.io'


class SentimentAnalyzer:

    # Initialize the class
    def __init__(self):
        pass

    # Return 'pos', 'neg', or 'neutral' based on the built-in sentiment
    # analyzer of TextBlob. Uses the polarity measure of the sentiment
    # analyzer to judge the data passed in.
    def trivially_analyze(self, data):
        blob = TextBlob(data)

        sentiment = blob.sentiment

        if 0 < sentiment.polarity <= 1.0:
            return 'pos'
        elif -1.0 <= sentiment.polarity < 0:
            return 'neg'
        elif sentiment.polarity == 0:
            return 'neutral'
