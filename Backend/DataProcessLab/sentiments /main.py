#disable=W0614
import TwitterRT
import pandas as pd
import scienceLAB
import os

def main():
    nTweets = 100
    #Routine for analysis using NLTK
    os.remove('/home/gabs/Backend/Backend/DataProcessLab/sentiments /inputs/result.csv')
    source = TwitterRT.AnalyzerTwiterRT()
    tweets = source.getCSV('iota', nTweets)
    lab = scienceLAB.Lab()
    tweets = pd.read_csv(
        '/home/gabs/Backend/Backend/DataProcessLab/sentiments /inputs/result.csv', encoding="ISO-8859-1")

    tweets = lab.cleanData(tweets)
    result = lab.sentimentAnalysis(tweets)
    print('nltk result')
    print(result)

    #====
    average, positive, negative, neutral = source.analysis('Trump', nTweets)

    print('TextBlob')
    print('Negative = ' + str(negative))
    print('Neutral = ' + str(neutral))
    print('Positive = ' + str(positive))

main()