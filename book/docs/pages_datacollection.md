# Data collection for distant reading

## Automated data collection

This repository has a focus on automated data collection with Python. To learn more about collecting podcast reviews and YouTube comments, please read the relevant sections under Skills (see page menu). At Maastricht University, we use our institutional Data Science Research Infrastructure (DSRI) to run code. This process is also explained under Skills. If you want to run code in a different environment, you may have to adjust the scripts accordingly. Please ask an expert for help if needed.

## Research strategies for data collection

Finding sufficient data for a topic you are interested in can be challening, also because relevant data may not include the most obvious keywords. Here is some advice to identifying useful data sets:

### Finding relevant search terms

Regardless of the search engine or platform you use to find content related to a topic, it is important to carefully develop your search terms. Mistakes that students often make
is that their search terms are either too broad or much too narrow. For example, searching for a podcast or video on "history" will give you more results than you can process, and it will not help you to create or answer a clear research question.
Instead of searching for “history,” you may want to search for “medieval history in France” to get a more manageable list of results. One example of the opposite challenge is that a student
of mine in a past course tried to find podcasts on "genital mutilation" but the few results that came up had absolutely no reviews they could analyse. In such cases, it is recommended
to branch out and consider related aspects such as female bodies, female sexuality, or violence against women. 

#### Use platform-integrated search features

When searching for videos or podcasts to scrape user comments, you can, of course, begin your search with the platform-integrated search features. Most people will find this easy on YouTube, but not everyone may be familiar with the App Store. Here, too, you can directly open the Apple podcasts app on your device or use the search box on the website for research, but you should be aware that reviews may only be visible when you open the show / episode website in your browser. This is a special challenge for MAC users as their machines tend to automatically re-direct to the app. Also, you have to consider that searching by keywords in the Apple Store
will only give you limited results because the search engine focuses on podcast titles and the short podcast descriptions. If your keyword is not mentioned, a relevant podcast may not come up as a result, so using external research tools is recommended.

### Aggregators, directories and recommendation sites

Websites like [Podchaser](https://www.podchaser.com/), [FeedSpot](https://podcasts.feedspot.com/), or [Listen Notes](https://www.listennotes.com/) list top-rated and specialised podcasts. You can often filter podcasts by subject, reviews, and popularity. In addition, blogs and (tech) news sites also regularly feature podcast recommendations, such as the [60 Best Podcasts (2024)](https://www.wired.com/story/best-podcasts/) presented by online magazine Wired.
After finding relevant podcasts, check whether they are available on Apple Podcasts. Most professional podcasts are on Apple. Similar services can also be used to identify popular YouTube channels or videos with many comments. Tech sides like Medium give advice on topics like ["9 Ways To Find Trending Topics On YouTube In 2024"](https://medium.com/@eddyballe/find-trending-topics-for-youtube-videos-df89100c85ae).

### Explore social media and discussion forums

Platforms like X, Mastodon, Threads, BlueSky, Reddit, and Facebook groups often have communities of video fans and podcast listeners who discuss and recommend shows.
Subreddits like r/podcasts can be a great source for finding highly recommended or niche podcasts. You can also consider asking other social media users for their
podcast or video recommendations on a specific topic.

### Generative AI (GenAI) for podcast and video search

In the MA DC course "Machines of Knowledge", students are explicitly allowed to use ChatGPT (or similar tools) to get Podcast recommendations for their topics.
However, the quality of the results that AI suggests varies greatly. It is, therefore, absolutely necessary to double-check if podcasts really exist, if they are available on Apple,
if they cover the topic of interests, and if URLs provided by AI are correct.

Students can directly prompt AI by asking for general recommendations, e.g.
      
           “Can you recommend podcasts about the history of technology available on Apple Podcasts?”*

In my experience, this often gives you few and not necessarily recent results, so it is better to explicitly ask for a certain number of podcasts and specify if you want
results from a particular time period or country:

           “Give me the top 5 podcasts produced after 2018 about ancient history that are available on Apple Podcasts.”*

Another strategy can be to provide AI with the names of podcasts that the student already knows to ask for similar content. Moreoever, AI can also help generate relevant
search terms for a subject to make finding podcasts via Google etc. easier. When a student wants to work with podcasts on “women’s rights,” for example, AI can suggest related topics like
“feminism,” “gender equality,” or “reproductive health” to broaden the search. In all cases where you use AI, it is vital to make transparent in graded assignments why you used it and what prompts
you gave the tool.
