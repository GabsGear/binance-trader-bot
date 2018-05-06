

from textblob import TextBlob as tb
import tweepy
import numpy as np
import csv


class AnalyzerTwiterRT():
    """This class process twitter in real time 

    Returns:
        sentiments 
    """
    __consumer_key = ''
    __consumer_secret = ''
    __access_token = ''
    __access_token_secret = ''

    def getTokens(self):
        return self.__consumer_key, self.__consumer_secret, self.__access_token, self.__access_token_secret

    def loginAPI(self):
        consumer_key, consumer_secret, access_token, access_token_secret = self.getTokens()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api

    #for get tweets in real time and export to a csv file
    def getCSV(self, keyword, nItens):
        api = self.loginAPI()
        csvFile = open('/home/gabs/Backend/Backend/DataProcessLab/sentiments /inputs/result.csv', 'a')
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['text'])
        for tweet in tweepy.Cursor(api.search,
                                q = keyword,
                                lang = "en").items(nItens):

            # Write a row to the CSV file. I use encode UTF-8
            csvWriter.writerow([tweet.text.encode('utf-8')])
            print (tweet.created_at, tweet.text)
        csvFile.close()

    #search tweets for textblob
    def search(self, keyword, nItens):
        api = self.loginAPI()
        return api.search(q=keyword, count=nItens)

    def analysis(self, keyword, nItens):
        #textblob analysis, return a average os sentiments
        public_tweets = self.search(keyword, nItens)
        analysis = None
        result = []
        positive = negative = neutral = 0
        for tw in public_tweets:
            analysis = tb(tw.text)
            result.append(analysis.sentiment.polarity)
            if(analysis.sentiment.polarity > 0):
                positive += 1
            if(analysis.sentiment.polarity == 0):
                neutral += 1
            else:
                negative += 1

        average = np.mean(result)
        return average, positive, negative, neutral