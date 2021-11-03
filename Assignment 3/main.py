# Programmer: Jason Mueller
# CS1026
# Assignment 3: Twitter Data Analysis 
# This is the file that will be controlling sentiment analysis and utilizing it.

from sentiment_analysis import compute_tweets

print("The return of the data from sentiment analysis: ")
print(compute_tweets('tweets.txt', 'keywords.txt'))