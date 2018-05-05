"""
    Consumer Key (API Key)	kNoBoo1wg6j9zZce2v5W2NFdh
    Consumer Secret (API Secret)	dZTYm4I1dqXYcXkM3CLK2qwEQihTU4DHtmn10oM1Z0rfqD3HEt
    Access Level	Read and write (modify app permissions)
    Owner	gabrielgheller1
    Owner ID	991736288238886912

    Access Token	991736288238886912-mH7f5OwdByFWXT6SUXnfxU83ZMXDKYG
    Access Token Secret	wQF5RAfA12pFrx1VBzenoBjys1iP91wxstyIdpTCLFr2K
    Access Level	Read and write
    Owner	gabrielgheller1
    Owner ID	991736288238886912
"""

from textblob import TextBlob as tb
import tweepy
import numpy as np
import csv


class AnalyzerTwiterRT():
    """This class process twitter in real time 

    Returns:
        sentiments 
    """
    __consumer_key = 'kNoBoo1wg6j9zZce2v5W2NFdh'
    __consumer_secret = 'dZTYm4I1dqXYcXkM3CLK2qwEQihTU4DHtmn10oM1Z0rfqD3HEt'
    __access_token = '991736288238886912-mH7f5OwdByFWXT6SUXnfxU83ZMXDKYG'
    __access_token_secret = 'wQF5RAfA12pFrx1VBzenoBjys1iP91wxstyIdpTCLFr2K'

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
            #print (tweet.created_at, tweet.text)
        csvFile.close()

    #search tweets for textblob
    def search(self, keyword, nItens):
        api = self.loginAPI()
        return api.search(q=keyword, count=nItens)

    def analysis(self, keyword):
        #textblob analysis, return a average os sentiments
        public_tweets = self.search(keyword)
        analysis = None
        result = []
        for tw in public_tweets:
            analysis = tb(tw.text)
            if(analysis.sentiment.polarity != 0.0):
                result.append(analysis.sentiment.polarity)

        average = np.mean(result)
        return average