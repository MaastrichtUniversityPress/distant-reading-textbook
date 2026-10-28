# check if countries have reviews at all

## Note: Multiprocessing has to be removed for live-coding in Pyodide

import requests
import re

def verify_countries(podcast_url, countries):
    # construct the URL based on the country code
    def construct_url(podcast_url, country_code):
        url_pattern = r"/[a-z]{2}/"  # any two-letter country code in the format /xx/
        return re.sub(url_pattern, f"/{country_code}/", podcast_url)
    
    # verify if a country has reviews for the podcast
    def verify_country_code(podcast_url, country_code):
        # construct the URL with the current country code
        url = construct_url(podcast_url, country_code)
        
        # HTTP GET request to the constructed URL
        response = requests.get(url)
    
        # check if the request was successful
        if response.status_code == 200:
            if '"Review"' in response.text:
                #print(f"The podcast has reviews for country code '{country_code}' at {url}.")
                return country_code
            else:
                #print(f"No reviews found for country code '{country_code}' at {url}.")
                return None
        else:
            #print(f"Failed to retrieve content for country code '{country_code}'. Status code: {response.status_code}")
            return None
    
    # check multiple countries one after another (adjusted for Pyodide)
    def pool_checks(podcast_url, countries):
        countries_reviewed = [verify_country_code(podcast_url, country) for country in countries]
        countries_reviewed = [country for country in countries_reviewed if country]
        return countries_reviewed
