import numpy as np
import pandas as pd
import re
import warnings
# Visualisation
import matplotlib.pyplot as plt
import matplotlib
from IPython.display import display
# NTLK
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
#nltk.download('wordnet')
#nltk.download('vader_lexicon')

matplotlib.style.use('ggplot')
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore")


class Lab:
    def cleanData(self, tweets):
        tweets['tweetos'] = ''
        # add tweetos first part
        for i in range(len(tweets['text'])):
            try:
                tweets['tweetos'][i] = tweets['text'].str.split(' ')[i][0]
            except AttributeError:
                tweets['tweetos'][i] = 'other'

        # Preprocessing tweetos. select tweetos contains 'RT @'
        for i in range(len(tweets['text'])):
            if tweets['tweetos'].str.contains('@')[i] == False:
                tweets['tweetos'][i] = 'other'

        # remove URLs, RTs, and twitter handles
        for i in range(len(tweets['text'])):
            tweets['text'][i] = " ".join([word for word in tweets['text'][i].split()
                                          if 'http' not in word and '@' not in word and '<' not in word])

        # remove ponctuations, put text in lower case and delete double space
        tweets['text'] = tweets['text'].apply(
            lambda x: re.sub('[!@#$:).;,?&]', '', x.lower()))
        tweets['text'] = tweets['text'].apply(lambda x: re.sub('  ', ' ', x))
        tweets['text'][1]
        return tweets

    def sentimentAnalysis(self, tweets):
        tweets['text_lem'] = [''.join([WordNetLemmatizer().lemmatize(re.sub(
            '[^A-Za-z]', ' ', line)) for line in lists]).strip() for lists in tweets['text']]

        #transform to a tf-idf matriz
        vectorizer = TfidfVectorizer(
            max_df=0.5, max_features=10000, min_df=10, stop_words='english', use_idf=True)

        sid = SentimentIntensityAnalyzer()

        tweets['sentiment_compound_polarity'] = tweets.text_lem.apply(
            lambda x: sid.polarity_scores(x)['compound'])
        tweets['sentiment_neutral'] = tweets.text_lem.apply(
            lambda x: sid.polarity_scores(x)['neu'])
        tweets['sentiment_negative'] = tweets.text_lem.apply(
            lambda x: sid.polarity_scores(x)['neg'])
        tweets['sentiment_pos'] = tweets.text_lem.apply(
            lambda x: sid.polarity_scores(x)['pos'])

        tweets['sentiment_type'] = ''
        tweets.loc[tweets.sentiment_compound_polarity >
                   0, 'sentiment_type'] = 'POSITIVE'
        tweets.loc[tweets.sentiment_compound_polarity ==
                   0, 'sentiment_type'] = 'NEUTRAL'
        tweets.loc[tweets.sentiment_compound_polarity <
                   0, 'sentiment_type'] = 'NEGATIVE'

        #PLot
        tweets_sentiment = tweets.groupby(['sentiment_type'])['sentiment_neutral'].count()
        tweets_sentiment.rename("",inplace=True)
        plt.subplot(221)
        tweets_sentiment.transpose().plot(kind='barh',figsize=(20, 20))
        plt.title('TRUMP', bbox={'facecolor':'0.8', 'pad':0})
        plt.show()

