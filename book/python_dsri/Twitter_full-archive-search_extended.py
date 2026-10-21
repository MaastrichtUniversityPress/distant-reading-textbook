# Extended script for full archive search with Twitter academic API
# based on a sample provided by Twitter
# for documentation, see https://developer.twitter.com/en/products/twitter-api/academic-research

import requests
import os
import json
import csv
import urllib # needed to merge strings to new URLs

# STEP 1: add bearer token for your academic Twitter API dev account

bearer_token = "YOUR TOKEN" # add your token here but do not share it with anyone

# STEP 2: define which API endpoint to query: "all" or "recent"

search_url="https://api.twitter.com/2/tweets/search/all"
token_url="https://api.twitter.com/2/tweets/search/all?next_token="
url=""
next_token=""

# Optional params: 
# start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields

# STEP 3: define query parameters and number of pages to be retrieved

# query example 1: (from:twitterdev -is:retweet) OR #twitterdev
# query example 2: ((from:Eurovision) OR #esc OR #esc2018) (#ISR OR #NettaBarzilai OR @NettaBarzilai) lang:en
# query example 3: (#lgbt OR #loveislove OR #pride) (#norway OR #oslo) lang:en
# query example 4: #lgbt OR #loveislove OR #pride OR #homophobia OR #PrideMonth) (#norway OR #oslo OR #oslopride OR #OsloPride2022 OR #oslolove) lang:en


query_params = {'query': '("miley" OR "cyrus" OR #miley OR #mileycyrus OR #robinthike OR "robin" OR @mileycyrus) ("vma2013" OR #vma2013 OR "performance" OR "vma" OR #vma OR #twerking OR "tv" OR "stage" OR "women" OR "children" OR "family" OR "culture" OR "black" OR "appropriation" OR "hip hop" OR "people of color" OR "dancers" OR "finger") lang:en',
                'tweet.fields': 'author_id,conversation_id,created_at',
                'expansions': 'geo.place_id',
                'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
                'user.fields': 'created_at,description,entities,id,location,name',
                'start_time': '2013-07-01T00:00:01.000Z',
                'end_time': '2013-10-01T23:59:59.000Z',
                'max_results':'500'}

pages = 200 # gives you 100,000 tweets for 500 per page 
token_list=[]

# STEP 4: authenticate

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

# STEP 5: connect to endpoint and run query

def connect_to_endpoint(url, params, next_token):
    try:
        if (len(token_list[-1]) >= 1):
            next_token=token_list[-1]
            target=[token_url, str(next_token)]
            url="".join(target)
            print(url)
        else:
            url = search_url
            print(url)
    except IndexError:
        url = search_url
        print(url)
    
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code == 200:
        print("Ready to go!")
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    json_data=response.json()
    next_token=json_data["meta"]["next_token"]
    token_list.append(next_token)
    
    print(token_list)
    
# STEP 6: write data to JSON file

    with open('C:\\Users\\mobarget\\Downloads\\VMA2013.json', 'a') as json_f:
        json.dump(json_data, json_f)
        print("JSON data written to file!")
        
# STEP 7: write tweet text only to TXT file

    all_tweets=json_data["data"]
    print("Your data set contains ", len(all_tweets), " tweets.")
    for t in all_tweets:
        
        text_only=t["text"]
        print("TWEET:", text_only)

        with open('C:\\Users\\mobarget\\Downloads\\VMA2013.txt', 'a', encoding="utf-8") as txt_f:
            txt_f.write(text_only)
            print("TEXT data written to file!")

def main():  
    for p in range(0, pages):
        try:
            json_response = connect_to_endpoint(url, query_params, next_token)
        except KeyError:
            print("No more tweets found!")
            break
    
if __name__ == "__main__":
    main()
