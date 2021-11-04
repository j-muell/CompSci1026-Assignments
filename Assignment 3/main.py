# Programmer: Jason Mueller
# CS1026
# Assignment 3: Twitter Data Analysis 
# This is the file that will be controlling sentiment analysis and utilizing it.

from sentiment_analysis import compute_tweets

print("Tweet Analysis Program\n-------------------------\n")

tweet_file = input("Please enter the name of the file containing the twitter data (including the .txt): ")
keyword_file = input("Please enter the name of the file containing the keywords (including the .txt): ")

print("\nThe return of the data from sentiment analysis:\n")
returned = compute_tweets(tweet_file, keyword_file)
# Eastern Data
print("Eastern Timezone Data\n-----------------------")
print("Average Happiness Value for Keyword Tweets: {:.2f}".format(returned[0][0]))
print("Total Keyword Tweets: {}".format(returned[0][1]))
print("Total Tweets: {}".format(returned[0][2]))
# Central Data
print("\nCentral Timezone Data\n---------------------")
print("Average Happiness Value for Keyword Tweets: {:.2f}".format(returned[1][0]))
print("Total Keyword Tweets: {}".format(returned[1][1]))
print("Total Tweets: {}".format(returned[1][2]))
# Mountain Data
print("\nMountain Timezone Data\n--------------------")
print("Average Happiness Value for Keyword Tweets: {:.2f}".format(returned[2][0]))
print("Total Keyword Tweets: {}".format(returned[2][1]))
print("Total Tweets: {}".format(returned[2][2]))
# Pacific Data
print("\nPacific Timezone Data\n----------------------")
print("Average Happiness Value for Keyword Tweets: {:.2f}".format(returned[3][0]))
print("Total Keyword Tweets: {}".format(returned[3][1]))
print("Total Tweets: {}\n".format(returned[3][2]))
