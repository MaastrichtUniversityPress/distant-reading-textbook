# Data scraping from YouTube

## Using YouTube comments as data source

Working with YouTube comments as a data source can be interesting because content published on YouTube ranges from academic talks to cooking instructions, sports commentary, and music videos, allowing us to capture user opinions on a wide range of issues. 

## Collecting YouTube comments using the Google API and Python

In order to work with YouTube comments, you need a Google API key that allows you to access this data (e.g. via a Python script). In my courses, I usually let students use my API keys for testing, but it is highly recommended that they sign up for their own keys later.

In addition to the API key, you will also need the URL of a playlist whose video comments you want to collect. For testing purposes, I typically use the URL of an Asian food playlist as a sample:

[Good Eats](https://www.youtube.com/playlist?list=PLbpi6ZahtOH6ibqudRCAPFl-MqAalKMJK)

The playlist is advertised as follows: "Share a meal with mukbang creators as they take you through a feast for the senses!"

The playlist contains 10 videos which have a total of 89,646 views. The comments to the videos are interesting because they are written in English as well as in several Asian languages. Also, the comments contain many emojis which can be used for a visual analysis, but which should ideally be cleaned before the comments are used for a text-focused analysis. As the playlist has a focus on food culture and the enjoyment of good meals, many of the emojis used are, naturally, related to eating. Here is an example of a comment that also exclusively relies on emojis: 

"🫕🥣🥣🥣 woo"

You should also keep in mind that it can be a problem that YouTube text comments are often very short and do not give you much context about the users.
One example of a very short text comment I scraped from one of the Good Eats videos is this:

"Nice 😋😋😋🥰..". 

When selecting a data set for your papers or final works, you should make sure that there is substantial content to work with. Perhaps food videos are not the best choice when your goal is to use Voyant tools for distant reading.

## Ready-made tools and their limitations

If you are not comfortable using code, you can also collect YouTube comments with several ready-made tools such as [Netlytic](https://socialmedialab.ca/apps/netlytic/). However, these tools typically have rate limits and / or do not allow you to capture all the available comments.

## Packages for R

If you prefer using R instead of Python, the [**tuber**](https://cran.r-project.org/web/packages/tuber/index.html) package is recommended for accessing YouTube data, allowing collection of video metadata and comments.

## Code demo video

[MONIKA WILL PROVIDE A DEMO VIDEO SOON!]
