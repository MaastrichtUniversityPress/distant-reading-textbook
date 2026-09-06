# Script for cleaning Tweets in Python, iterating through all files in a repository
# based on the tutorial provided by https://catriscode.com/2021/05/01/tweets-cleaning-with-python/
# adapted and extended by Monika Barget in November 2022

import numpy as np
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import requests
import os

# STEP 1: define directory for input and output files

directory = 'C:\\Users\\mobarget\\Downloads\\CONVERT\\'
    
# STEP 2: define custom stopwords (OPTIONAL)

# a) From GITHUB:

#url = "https://gist.githubusercontent.com/sebleier/554280/raw/7e0e4a1ce04c2bb7bd41089c9821dbcf6d0c786c/NLTK's%2520list%2520of%2520english%2520stopwords"
#resp = requests.get(url)
#my_stopwords=resp.text

# b) From NLTK:

#my_stopwords=stopwords.words('en') # multilingual: 'en_fr_de'
#my_stopwords.extend(['@']) # extend list if necessary
#print(my_stopwords)

# c) Manual list:

my_stopwords = ["http", "https", "#", "@"]

# STEP 3: define function with cleaning operations

def clean_tweet(tweet):
    if type(tweet) == float:
        return " "
    temp = tweet.lower()
    temp = re.sub("I'm", "I am", temp) # to avoid removing contractions in english
    temp = re.sub("We're", "We are", temp) # to avoid removing contractions in english
    temp = re.sub("You're", "You are", temp) # to avoid removing contractions in english
    temp = re.sub("She's", "She is", temp) # to avoid removing contractions in english
    temp = re.sub("He's", "He is", temp) # to avoid removing contractions in english
    temp = re.sub("They're", "They are", temp) # to avoid removing contractions in english
    temp = re.sub("Don't", "Do not", temp) # to avoid removing contractions in english
    temp = re.sub("Won't", "Will not", temp) # to avoid removing contractions in english
    temp = re.sub("It's", "It is", temp) # to avoid removing contractions in english
    temp = re.sub("/[A-Za-z0-9_]+"," ", temp)
    temp = re.sub("\n"," ", temp)
    temp = re.sub("\r"," ", temp)
    temp = re.sub(r'http\S+', ' ', temp)
    temp = re.sub('[()!?]', ' ', temp)
    temp = re.sub('\[.*?\]',' ', temp)
    temp = re.sub("[^a-z0-9]"," ", temp)
    temp = temp.split()
    temp = [w for w in temp if not w in my_stopwords]
    temp = " ".join(word for word in temp)
    return temp

# STEP 4: call function and get results

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        with open(f, encoding="utf-8") as infile:
            tweets = infile.readlines()
            results = [clean_tweet(tw) for tw in tweets]
            results
            
# STEP 5: write results to new file

            f_split=os.path.splitext(filename)[0]
            print(f_split)

            outfile=os.path.join(directory + f_split +'_cleaned-with-Python' +'.txt')
            print(outfile)

            with open(outfile, 'a', encoding="utf-8") as new_f:
                for r in results:
                    new_f.write(r + '\n')
    else:
        continue

print("done")
