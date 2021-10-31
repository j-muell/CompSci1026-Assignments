# Programmer: Jason Mueller
# CS 1026
# Assignment 3: Tweet and happiness checker
# This file will be doing the main workload on evaluating the tweets. Calculating timezone, cleaning up the tweets, checking for
# the keywords, and giving evaluation to the words, etc.

import main

# -- CONSTANTS --


def tweet_cleaner(tweet_word):
    return "".join(u for u in tweet_word if u not in("?","!","#",",","/","&","$","@","\"","'",":",";","=",".","(",")","%","*"))
    # this function uses an interable with the .join() function to get rid of any punctuation in the tweet. I felt this was
    # easier than using the .replace() funcation

def get_longlat(full_tweet):
    result = full_tweet[full_tweet.find('[')+1:full_tweet.find(']')]
    result = result.split()
    result[0] = result[0].replace(',', '')
    return result

def determine_timezone():
    pass


def compute_tweets(tweets_file, keywords_file):
    try: 
        tweets = open(tweets_file)
        keywords = open(keywords_file)

        tweet_list = tweets.readlines()
        


    except FileNotFoundError as excpt:
        print(excpt)
        print("One or more of the files you entered does not exist.")

