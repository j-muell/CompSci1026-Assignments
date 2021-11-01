# Programmer: Jason Mueller
# CS 1026
# Assignment 3: Tweet and happiness checker
# This file will be doing the main workload on evaluating the tweets. Calculating timezone, cleaning up the tweets, checking for
# the keywords, and giving evaluation to the words, etc.

import main
from string import punctuation
import re

# -- CONSTANTS --

eastern_total_tweets = 0
central_total_tweets = 0
mountain_total_tweets = 0
pacific_total_tweets = 0

eastern_total_keywordTweets = 0
central_total_keywordTweets = 0
mountain_total_keywordTweets = 0
pacific_total_keywordTweets = 0


def get_longlat(full_tweet):
    # takes in the entire data string and separates out the long and lat into a list, then returns the list. also removes comma
    result = full_tweet[full_tweet.find('[')+1:full_tweet.find(']')]
    result = result.split()
    result[0] = result[0].replace(',', '')
    return result

def determine_timezone():
    get_longlat()

def tweet_cleaner(tweet_word):
    return tweet_word.lower().strip(punctuation)
    # using an imported punctutation variable, i use .strip() to take all leading and trailing punctuation out of the given word

def tweet_split_and_clean(tweet_sentence):
    # this function will take the tweet sentence, clean all the periods and split the sentence into words in a list. Then it
    # takes the list and cleans the front and back of the word for any punctuation.
    if '.' in tweet_sentence:
        tweet_sentence = tweet_sentence.replace('.', ' ')
    tweet_words = tweet_sentence.split()
    for index, word in enumerate(tweet_words):
        tweet_words[index] = tweet_cleaner(word)
        
    tweet_words[:] = [x for x in tweet_words if x.strip()]
    return tweet_words

def input_splitting(data_string):
    # this function uses the re module - regular expression operations - to eliminate everything within square brackets
    # including the brackets themselves. This leaves exactly 23 characters before the main tweet, each and every time.
    # It then takes this first fix and returns the first fix spliced after 23 characters, leaving just the sweet as the
    # return string.
    # I believe using re was the best way to do this otherwise I would have had 20 lines of code just to remove the long lat areas.
    # This function then takes the fixed string and sends it to tweet split and clean, which also calls tweet cleaner in itself.
    # the full result is given in a list format, ready to be used to test the words.
    first_fix = re.sub("[\(\[].*?[\)\]]", "", data_string)
    full_fix = first_fix[23:]
    return tweet_split_and_clean(full_fix)




def compute_tweets(tweets_file, keywords_file):
    try: 
        tweets = open(tweets_file)
        with open('keywords.txt') as f:
            keyword_dict = {k: int(v) for line in f for k,v in [line.strip().split(',')]}
        # instead of opening this file normally i am using dictionary comprehension to turn the entire file into a dictionary
        # instead of the standard list which would come from using the readlines() function.

        tweet_list = tweets.readlines()
        
        


    except FileNotFoundError as excpt:
        print(excpt)
        print("One or more of the files you entered does not exist.")

