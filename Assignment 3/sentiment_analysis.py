# Programmer: Jason Mueller
# CS 1026
# Assignment 3: Tweitter data analysis and happiness checker
# This file will be doing the main workload on evaluating the tweets. Calculating timezone, cleaning up the tweets, checking for
# the keywords, and giving evaluation to the words, etc.

from string import punctuation
import re

# Constants for Timezone Detection
    # eastern begin
p1 = [49.189787, -67.444574]
p2 = [24.660845, -67.444574]
    # Central begin, eastern end
p3 = [49.189787, -87.518395]
# p4 = [24.660845, -87.518395]      - Not needed
    # Mountain begin, central end
p5 = [49.189787, -101.998892]
# p6 = [24.660845, -101.998892]     - Not needed
    # Pacific begin, mountain end
p7 = [49.189787, -115.236428]
# p8 = [24.660845, -115.236428]     - Not needed
    # pacific end, still pacific
p9 = [49.189787, -125.242264]
# p10 = [24.660845, -125.242264]

def get_longlat(full_tweet):
    # takes in the entire data string and separates out the long and lat into a list, then returns the list. also removes comma
    result = full_tweet[full_tweet.find('[')+1:full_tweet.find(']')]
    result = result.split()
    result[0] = result[0].replace(',', '')
    return result

def determine_timezone(tweet_list):
    
    for index, tweet in enumerate(tweet_list): # takes in index and tweet data and creates a for loop
        long_lat = get_longlat(tweet) # determines the longlat for the tweet that is currently needed to work on
        if float(long_lat[0]) <= float(p1[0]) and float(long_lat[0]) >= float(p2[0]):
            if float(long_lat[1]) <= float(p1[1]) and float(long_lat[1]) > float(p3[1]):
                # this is testing for the eastern region
                eastern_list.append(tweet_list[index])
            elif float(long_lat[1]) <= float(p3[1]) and float(long_lat[1]) > float(p5[1]):
                # testing for the central region
                central_list.append(tweet_list[index])
            elif float(long_lat[1]) <= float(p5[1]) and float(long_lat[1]) > float(p7[1]):
                # testing for mountain region
                mountain_list.append(tweet_list[index])
            elif float(long_lat[1]) <= float(p7[1]) and float(long_lat[1]) >= float(p9[1]):
                # testing for pacific region
                pacific_list.append(tweet_list[index])
            else:
                # if nothing is found, continue to the next element in the tweet data and do nothing
                continue
        else:
            # if nothing is found for the longitude, then also continue
            continue

def calculations(keyword_dict, tweet_list):
    # - Constants for caclulations and returns
    total_tweets = 0
    total_keyword_tweets = 0
    average_happiness = 0
    happiness_sum = 0

    for entry in tweet_list: # saying for each piece of the tweet list
        word_list = input_splitting(entry) # run through the input splitting for list of words
        total_tweets += 1 # add one to total tweets
        keyword_happened_counter = 0 # this is used to know if the word list has already had a keyword tweet. Needs to be
        # reset to 0 again in this spot.
        for word in word_list:  # for each word in that word list 
            for key, value in keyword_dict.items(): # take the key and respective value for each item in the dict
                # print("key:", key, "val:", value)
                if word == key: # if the word we got is the same as the key value
                    if keyword_happened_counter == 0: # and the keyword counter hasnt gone up
                        total_keyword_tweets += 1 # add one to the total keyword tweets
                        keyword_happened_counter += 1 # then add one to keyword happened counter
                    happiness_sum += value # and, if we have a keyword tweet, no matter what add to the happiness sum
                else:
                    continue # if we don't have a word == key, continue iterating.
    if total_keyword_tweets != 0:
        average_happiness = happiness_sum / total_keyword_tweets # calculation for the average happiness value
    else:
        average_happiness = 0
    return [average_happiness, total_keyword_tweets, total_tweets] # returning a tuple of info in proper order

def final_calculation(eastern, central, mountain, pacific):
    final_calculations = []
    final_calculations.append(eastern)
    final_calculations.append(central)
    final_calculations.append(mountain)
    final_calculations.append(pacific)
    return final_calculations

                
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
        
    tweet_words[:] = [x for x in tweet_words if x.strip()] # list comprehension to finish up the tweet words list.
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




def compute_tweets(tweets, keywords):
    try:
        # - Lists 
        global eastern_list, central_list, mountain_list, pacific_list
        eastern_list = []
        central_list = []
        mountain_list = []
        pacific_list = []
        with open(tweets, encoding="utf-8", errors="ignore") as f: # opens the file 
            tweet_list = f.read().splitlines() # reads and splitlines the file. Gets rid of the \n
        with open(keywords, encoding="utf-8", errors="ignore") as f:
            keyword_dict = {k: int(v) for line in f for k,v in [line.strip().split(',')]}
        # instead of opening this file normally i am using dictionary comprehension to turn the entire file into a dictionary
        # instead of the standard list which would come from using the readlines() function.
               
        determine_timezone(tweet_list) # this will run the function to split all pieces of the file into region specific ones
        eastern = calculations(keyword_dict, eastern_list)
        central = calculations(keyword_dict, central_list)
        mountain = calculations(keyword_dict, mountain_list)
        pacific = calculations(keyword_dict, pacific_list)

        return final_calculation(eastern, central, mountain, pacific)
        

    except FileNotFoundError as excpt:
        empty_list = [] 
        print(excpt)
        print("One or more of the files you entered does not exist.")
        return empty_list
