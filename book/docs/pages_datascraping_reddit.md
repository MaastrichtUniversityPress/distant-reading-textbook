# Using Reddit for research

# Ethical and technical challenges

Reddit, once seen as a user-driven community space, has recently evolved into a more monetised platform. They have, for instance, entered into an ["expanded partnership"](https://blog.google/inside-google/company-announcements/expanded-reddit-partnership/) with Google. This challenges users and researchers alike. One content-related problem in working with Reddit data can now be that ads are integrated in user feeds and that drawing lines between community engagement and profit generation may be difficult. A more technical problem is that the Reddit API has created new barriers for developers and academics as outlined in the [**API and Developer Terms**](https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki). When using Reddit, it is important that you use a **registered OAuth token** for authentication. After scraping data, you have to be aware that Reddit requires you to delete content from your own storage if the content (e.g. a post, comment or entire user profile) gets deleted on their site, which means that keeping Reddit data you collected for later reuse or even data sharing is not an option. It’s recommended to delete stored Reddit data every 48 hours to stay compliant. Moreover, the Reddit API limits the number of API requests that you can send per minute. In November 2024, the rate is at **100 requests per minute** for each OAuth client ID.

## Pushshift Reddit documentation

One way to access slightly older Reddit data is the [PullPush Reddit API Documentation](https://www.pullpush.io/). 

:hammer_and_wrench: More detailed information to follow! :hammer_and_wrench:

## R and Python packages

For users comfortable with R or Python, the following packages allow data collection from Reddit in compliance with their API policies:

- [PRAW (Python Reddit API Wrapper)](https://github.com/praw-dev/praw) gathers Reddit posts, comments, and metadata. However, it only scrapes up to 1000 posts or comments in total (according to users).
- [RedditExtractoR](https://github.com/ivan-rivera/RedditExtractor) performs Reddit data collection in R.

:hammer_and_wrench: Test script we used in 2023 and see if it is still functional!