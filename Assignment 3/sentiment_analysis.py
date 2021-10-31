# Programmer: Jason Mueller
# CS 1026
# Assignment 3: Tweet and happiness checker
# This file will be doing the main workload on evaluating the tweets. Calculating timezone, cleaning up the tweets, checking for
# the keywords, and giving evaluation to the words, etc.

import main
from string import punctuation

# -- CONSTANTS --


def tweet_cleaner(tweet_word):
    return tweet_word.lower().strip(punctuation)
    # using an imported punctutation variable, i use .strip() to take all leading and trailing punctuation out of the given word


def get_longlat(full_tweet):
    result = full_tweet[full_tweet.find('[')+1:full_tweet.find(']')]
    result = result.split()
    result[0] = result[0].replace(',', '')
    return result

def determine_timezone():
    get_longlat()


def tweet_split_and_clean(tweet_sentence):
    if '.' in tweet_sentence:
        tweet_sentence = tweet_sentence.replace('.', ' ')
    tweet_words = tweet_sentence.split()
    for index, word in enumerate(tweet_words):
        tweet_words[index] = tweet_cleaner(word)
        
    tweet_words[:] = [x for x in tweet_words if x.strip()]
    return tweet_words

    

def compute_tweets(tweets_file, keywords_file):
    try: 
        tweets = open(tweets_file)
        keywords = open(keywords_file)

        tweet_list = tweets.readlines()
        


    except FileNotFoundError as excpt:
        print(excpt)
        print("One or more of the files you entered does not exist.")

