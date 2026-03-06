# Social Media Analysis with Twitter

:no_entry_sign: 

Some of the scripts and data shared here relate to social media analysis with Twitter. The Twitter academic API access was used to harvest the data. It is important to note that the original academic Twitter API is no longer accessible as a consequence of Elon Musk's restructuring of the platform, which is now known as X. Therefore, the following documentation merely serves as an archive and general example of social media scraping. The Python script I used to collect Twitter data until 2023 was the following:

- [Python script for Twitter full archive search](https://github.com/MonikaBarget/DistantReading/blob/main/Twitter_full-archive-search_extended.py)

## The VMA2013 Scandal - Background

As an example of a prominent social media event that can be analyzed via distant reading, I have chosen the 2013 MTV music awards performance by Miley Cyrus and Robin Thicke. The controversial performance was extensively covered on Twitter and still incited comments and comparisons years later.

At the time of the actual event in 2013, one of the most frequently retweeted posts was [a photo of the Smith family's alleged reaction](https://twitter.com/theJeremyVine/status/372040980910067713) shared by @thejeremyvine. The photo was taken out of context but expressed how a lot of Twitter users felt about the performance.

In 2022, a [post relating to a mannequin wearing an imitation of Miley Cyrus's VMA2013 outfit](https://twitter.com/milesholy/status/1488596498753499142) got 3,608 retweets and 35,700 likes. According to the Spanish-language post, dressing the mannequin in this way was meant as criticism. The post also stated that Miley's reaction was to take a photo of herself "with a mannequin that looked like a donkey."

## Characteristics of the VMA2013 Twitter Reactions

In general, the Twitter controversy started by the VMA 2013 was very much an *image war* in which people shared videos, original photographs, collages, or memes to express their opinions. When collecting a data set for distant reading, it is therefore vital to take the high number of tweets without text into account and to harvest tweets relating to several keywords and hashtags.

Another challenge of this particular controversy is that the number of replies or commented retweets considerably outweighs the number of original tweets (using clearly identifiable hashtags), which means some ready-made tools for harvesting tweets may only capture a tiny fraction of what is available. The Web Data Research Assistant developed in Southampton, for instance, tends to ignore text in replies. Gathering tweets on different aspects of the VMA2013 debate (e.g., the impact of the show on children), I was able to collect 33,006 initial items via WDRA, but having deleted duplicates, tweets that only had visual content, and replies that came in as empty cells, only 320 unique tweets with meaningful content were left. Depending on your research question, WDRA may therefore not be the best tool to use and you should consider alternatives. The most efficient way of harvesting social media data is, of course, to use the official APIs and scripts (e.g., in Python and R) that can be customized to suit your case studies. Using code, however, requires advanced skills.

## Building Twitter Queries with the Twitter API v2 and Python

As Miley Cyrus's performance incited 306,000 tweets per minute on the day of the event, the data that we can collect are "big data," indeed. However, this does not mean that such a huge data set is easy to analyze. On the contrary, some central keywords such as the names of the performers will become even more prominent in the data set the more tweets we collect, which can make using a word cloud and other visualization tools very difficult. Most reactions are short and either express support or disgust, but they do not offer a deeper reflection. Finding tweets that explicitly address sub-themes such as the representation of women or cultural appropriation in the data therefore requires a more careful pre-selection.

### 1) First Twitter Query with More Generic Keywords

```
query = '("miley" OR "cyrus" OR #miley OR #mileycyrus OR #robinthike OR @mileycyrus) ("vma2013" OR #vma2013 OR "performance" OR "vma" OR #vma OR "tv") lang:en'
```

### 2) Second Twitter query with more specific keywords

For the second query, I defined more precise ```query_params```:

```
{'query': '("miley" OR "cyrus" OR #miley OR #mileycyrus OR #robinthike OR "robin" OR @mileycyrus) ("vma2013" OR #vma2013 OR "performance" OR "vma" OR #vma OR #twerking OR "tv" OR "stage" OR "women" OR "children" OR "family" OR "culture" OR "black" OR "appropriation" OR "hip hop" OR "people of color" OR "dancers" OR "finger") lang:en',
                'tweet.fields': 'author_id,conversation_id,created_at',
                'expansions': 'geo.place_id',
                'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
                'user.fields': 'created_at,description,entities,id,location,name',
                'start_time': '2013-07-01T00:00:01.000Z',
                'end_time': '2013-10-01T23:59:59.000Z',
                'max_results':'500'}
```

With ``` pages = 200 ```, the script retrieves 100,000 tweets with 500 per page.

### 3) Third Twitter query with specific keywords but excluding retweets

```
'query': '("miley" OR "cyrus" OR #miley OR #mileycyrus OR #robinthike OR "robin" OR @mileycyrus) 
                ("vma2013" OR #vma2013 OR "performance" OR "vma" OR #vma OR #twerking OR "tv" OR "stage" OR "women"
OR "children" OR "family" OR "culture" OR "black" OR "appropriation" OR "hip hop" OR "people of color" OR "dancers" OR "finger") lang:en -is: retweet'
```

For text analysis, the second data set with specific keywords but still including retweets proved the most interesting as it best captured the polarisation of the debate. In all cases, the search focused on the time between 1 July 2013 and 1 October 2013, thus covering debates before and directly after the performance. 

## Challenges of the text analysis in Voyant
  
## Challenges of Text Analysis in Voyant

1. Frequent use of slang, e.g., *"molly" for the drug MDMA / Ecstasy*: *Miley Cyrus Was She On Molly During the VMA Show? #molly #MileyCyrus #VMAs*
2. Visual communication through images and emojis is lost in the text analysis.
3. Many tweets are very short, e.g., *Miley Cyrus on chatty man tonight. should be interesting #twerking*.
4. Trending hashtags linked with the event were also (ab)used to promote porn or create cross-references to other musicians in the community, e.g., *#MileyCyrus #Thicke #Gaga #1D and #Bieber sound so much better with these #Beats*.
5. Twitter users heavily relied on sharing links to video clips relating to the event (many URLs in the data set).