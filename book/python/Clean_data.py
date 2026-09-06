# Script for cleaning Tweets and other social media data in Python
# based on the tutorial provided by https://catriscode.com/2021/05/01/tweets-cleaning-with-python/
# written by Monika Barget, November 2022

import numpy as np
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import requests

# STEP 1: read tweets from text file

with open('C:\\Users\\####\\Downloads\\VMA2013_100000tweets_cleaned.txt', encoding="utf-8") as f:
    tweets = f.readlines()

# STEP 2: define custom stopwords (only needed when using a tool that does not include stopword handling)

# a) Import stopword from GITHUB

#url = "https://gist.githubusercontent.com/sebleier/554280/raw/7e0e4a1ce04c2bb7bd41089c9821dbcf6d0c786c/NLTK's%2520list%2520of%2520english%2520stopwords"
#resp = requests.get(url)
#my_stopwords=resp.text

# b) Import stopwords from NLTK

#my_stopwords=stopwords.words('en') # multilingual: 'en_fr_de'
#my_stopwords.extend(['@']) # extend list if necessary
#print(my_stopwords)

# c) Define a manual stopword list (useful for special words and characters in a specific data set)

my_stopwords = ["http", "https", "#", "@"]

# STEP 3: define function with cleaning operations

def clean_tweet(tweet):
    if type(tweet) == np.float: # deprecated?? Find new syntax!
        return ""
    temp = tweet.lower()
    temp = re.sub("'", "", temp) # to avoid removing contractions in english
    temp = re.sub("/[A-Za-z0-9_]+","", temp)
    temp = re.sub(r'http\S+', '', temp)
    temp = re.sub('[()!?]', ' ', temp)
    temp = re.sub('\[.*?\]',' ', temp)
    temp = re.sub("[^a-z0-9]"," ", temp)
    temp = temp.split()
    temp = [w for w in temp if not w in my_stopwords]
    temp = " ".join(word for word in temp)
    return temp

# STEP 4: call function and get results
  
results = [clean_tweet(tw) for tw in tweets]
results

# STEP 5: write results to new file

with open('C:\\Users\\mobarget\\Downloads\\VMA2013_100000tweets_cleaned-with-Python.txt', 'a', encoding="utf-8") as new_f:
    for r in results:
        new_f.write(r)
    
print("done")   
