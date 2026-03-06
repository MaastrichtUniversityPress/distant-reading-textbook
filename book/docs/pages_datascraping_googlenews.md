# Scraping news items via the Google API

## Use cases and limitations

When working on contemporary political and social issues, getting "treding" news via the Google API can be one solution for a relatively fast data collection. Unfortunately, the way in which Google News entries are ranked is not entirely transparent. The [Google Publisher Help Center](https://support.google.com/news/publisher-center/answer/9606702?hl=en) states that "ranking in Google News is determined algorithmically" and mentions "relevance of content", "prominence", "authoritativeness", "freshness", "location" and "language" as the most important factors. However, criteria such as "freshness" are not specified and scraping of news items shows that many articles are ranked highly for several days in a row. This is why working with Google News always requires a critical reflection on the data retrieved.

## Overview of available Google News API scraper on Github

Github has a helpful [overview of code and apps](https://github.com/topics/google-news-scraper) that can be used to scrape Google News. Most of these respositories provide information on scraping metadata, but not the actual text behind the articles (see information below). A considerable number of the scripts for extracting news via the Google API are written in Python, a programming language that is very popular in the digital humanities and social sciences. What you have to keep in mind is that most of the scripts are written by developers who are not paid for maintenance and who may therefore abandon the scripts after a while. API changes on the side of Google or upgrades for dependent packages can, therefore, result in depricated code.
 
## Options to scrape Google News content by time or region

Several forum discussions, e.g. on Stackoverflow, cover the different scraping options for Google News and the challenges they may pose. The parameters that the Google News API allows for data selection are documented [here](https://serpapi.com/google-news-api). One problem is that Google News now only permit a collection of 100 items max. per query, and it is unfortunately not possible to scrape news by the hour (see [this question](https://stackoverflow.com/questions/73072802/web-scraping-articles-from-google-news) on Stackoverflow and the relevant responses. The smallest time frame that can be selected is one day. But collecting news across a longer time frame is still possible when looping through a longer period of time. It can also help to combine scraping data per day with scraping data per country as the default setting in Google news is to collect US news.

To scrape Google news by country, you can iterate through the list of countries in which Google services are supported. The full list of countries is available for download here: [https://serpapi.com/google-countries](https://serpapi.com/google-countries)

However, in many cases, all countries across the world are shown the exact same news items, especially where international crises are concerned. Testing data scraping for an MA thesis, the student found that Afghanisatan and Australia, for instance, were shown the exact same top-60 news items for the keyword "Gaza" on October 7, 2023, to October 8, 2023, shortly after the conflict between Israel and Palestine escalated:

| title                                                                                                                                     | published date                | publisher.title                      |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------ |
| Hamas surprise attack out of Gaza stuns Israel and leaves hundreds dead in fighting, retaliation - The Associated Press                   | Sat, 07 Oct 2023 07:00:00 GMT | The Associated Press                 |
| In focus: The war in Gaza - UN Women                                                                                                      | Sat, 07 Oct 2023 07:00:00 GMT | UN Women                             |
| Timeline of conflict between Israel and Palestinians in Gaza - Reuters                                                                    | Sat, 07 Oct 2023 07:00:00 GMT | Reuters                              |
| Netanyahu says Israel is ‘at war’ after Hamas launches surprise air and ground attack from Gaza - CNN                                     | Sat, 07 Oct 2023 07:00:00 GMT | CNN                                  |
| Israel-Palestine escalation updates: Gaza under bombardment | Israel War on Gaza News - Al Jazeera English                                | Sat, 07 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| Israel/OPT: Civilians on both sides paying the price of unprecedented escalation in hostilities between Israel and Gaza ... - amnesty.org | Sat, 07 Oct 2023 07:00:00 GMT | amnesty.org                          |
| What is Hamas and why is it fighting with Israel in Gaza? - BBC.com                                                                       | Sat, 07 Oct 2023 15:58:40 GMT | BBC.com                              |
| Israel battles Hamas militants as death toll nears 1,200 - The Associated Press                                                           | Sun, 08 Oct 2023 07:00:00 GMT | The Associated Press                 |
| Facts and figures: Women and girls during the war in Gaza - UN Women                                                                      | Sat, 07 Oct 2023 07:00:00 GMT | UN Women                             |
| Why this Israel-Gaza conflict is so complicated for Biden - CNN                                                                           | Sat, 07 Oct 2023 07:00:00 GMT | CNN                                  |
| Israel retaliates after Hamas attacks, deaths pass 1100 - Reuters                                                                         | Sun, 08 Oct 2023 07:00:00 GMT | Reuters                              |
| Israel declares state of war, attacks on Gaza intensify - Al Jazeera English                                                              | Sun, 08 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| Israel retaliation kills 230 Palestinians after Hamas operation - Al Jazeera English                                                      | Sat, 07 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| Israel formally declares war against Hamas as it battles to push militants off its soil - CNN                                             | Sun, 08 Oct 2023 07:00:00 GMT | CNN                                  |
| Israel vows 'mighty vengeance' after surprise attack - Reuters                                                                            | Sat, 07 Oct 2023 07:00:00 GMT | Reuters                              |
| The history of Gaza in 2 minutes - CNN                                                                                                    | Sat, 07 Oct 2023 07:00:00 GMT | CNN                                  |
| Fears of a ground invasion of Gaza grow as Israel vows ‘mighty vengeance’ - Al Jazeera English                                            | Sat, 07 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| Gaza Strip suffers deadliest day in 15 years after Hamas attack - Reuters                                                                 | Sun, 08 Oct 2023 07:00:00 GMT | Reuters                              |
| Israel-Hamas war updates: Death toll rises as Israeli jets pound Gaza - Al Jazeera English                                                | Sun, 08 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| War grips Israel, Gaza after surprise Hamas attack and Israeli retaliation - PBS NewsHour                                                 | Sat, 07 Oct 2023 07:00:00 GMT | PBS NewsHour                         |
| Israel-Palestine history: The deep roots of the Israel-Gaza conflict - Vox.com                                                            | Sat, 07 Oct 2023 07:00:00 GMT | Vox.com                              |
| Israel-Gaza Conflict: Air-Raid Sirens in Israel Warn of Continued Strikes on Sunday - The New York Times                                  | Sat, 07 Oct 2023 07:00:00 GMT | The New York Times                   |
| Gaza Has Suffered Under 16-Year Blockade - The New York Times                                                                             | Sat, 07 Oct 2023 07:00:00 GMT | The New York Times                   |
| What to know as conflict erupts between Hamas and Israel after deadly attack, retaliation - PBS NewsHour                                  | Sat, 07 Oct 2023 07:00:00 GMT | PBS NewsHour                         |
| Desert horror: Music festival goers heard rockets, then Gaza militants fired on them and took hostages - CNN                              | Sat, 07 Oct 2023 07:00:00 GMT | CNN                                  |
| What happened in Israel? A breakdown of how Hamas attack unfolded - Al Jazeera English                                                    | Sat, 07 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| An Attack From Gaza and an Israeli Declaration of War. Now What? - The New York Times                                                     | Sat, 07 Oct 2023 07:00:00 GMT | The New York Times                   |
| There is nothing surprising about Hamas’s operation - Al Jazeera English                                                                  | Sun, 08 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| Gaza: MSF provides medical care and donates supplies amid intense conflict - Doctors Without Borders (MSF-USA)                            | Sun, 08 Oct 2023 07:00:00 GMT | Doctors Without Borders (MSF-USA)    |
| An Israeli airstrike kills 19 members of the same family in a southern Gaza refugee camp - The Associated Press                           | Sun, 08 Oct 2023 07:00:00 GMT | The Associated Press                 |
| What is Hamas? A simple guide to the armed Palestinian group - Al Jazeera English                                                         | Sun, 08 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| Israel flattens Palestine Tower amid deadly Gaza bombardment - Al Jazeera English                                                         | Sat, 07 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| Escalation in the Gaza Strip and Israel | Flash Update #2 [EN/AR/HE] - occupied Palestinian territory - ReliefWeb                         | Sun, 08 Oct 2023 07:00:00 GMT | ReliefWeb                            |
| Israeli strikes flatten buildings, mosques in Gaza - Al Jazeera English                                                                   | Sun, 08 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| Resources for Educators, Families to Discuss the Events in Israel and Gaza with Students - San Diego County Office of Education           | Sat, 07 Oct 2023 07:00:00 GMT | San Diego County Office of Education |
| Why the Palestinian group Hamas launched an attack on Israel? All to know - Al Jazeera English                                            | Sat, 07 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| Netanyahu Bears Responsibility for This Israel-Gaza War - Haaretz Editorial - Haaretz                                                     | Sun, 08 Oct 2023 07:00:00 GMT | Haaretz                              |
| UNRWA Situation Report # 1 on the situation in the Gaza Strip - unrwa                                                                     | Sat, 07 Oct 2023 07:00:00 GMT | unrwa                                |
| Israel faces 'long, difficult war' after Hamas attack from Gaza - BBC.com                                                                 | Sat, 07 Oct 2023 07:00:00 GMT | BBC.com                              |
| No place for Gaza residents to flee after Israel declares war, bombs homes - Al Jazeera English                                           | Sun, 08 Oct 2023 07:00:00 GMT | Al Jazeera English                   |
| What to know about the Gaza Strip - DW (English)                                                                                          | Sun, 08 Oct 2023 07:00:00 GMT | DW (English)                         |
| Israel-Gaza conflict: Slideshow - ABC News                                                                                                | Sat, 07 Oct 2023 18:58:58 GMT | ABC News                             |
| For years, Netanyahu propped up Hamas. Now it’s blown up in our faces - The Times of Israel                                               | Sun, 08 Oct 2023 07:00:00 GMT | The Times of Israel                  |
| Gaza: Everything you need to know about the besieged Palestinian enclave - Middle East Eye                                                | Sat, 07 Oct 2023 07:00:00 GMT | Middle East Eye                      |
| Maps: Tracking the Attacks in Israel and Gaza - The New York Times                                                                        | Sat, 07 Oct 2023 07:00:00 GMT | The New York Times                   |
| Massive explosion as Gaza high-rises destroyed by jets - BBC.com                                                                          | Sat, 07 Oct 2023 07:00:00 GMT | BBC.com                              |
| Israel attack: PM says Israel at war after 250 killed in attack from Gaza - BBC.com                                                       | Sat, 07 Oct 2023 07:00:00 GMT | BBC.com                              |
| The West's hypocrisy towards Gaza's breakout is stomach-turning - Middle East Eye                                                         | Sun, 08 Oct 2023 07:00:00 GMT | Middle East Eye                      |
| What is Hamas, how does it control the Gaza Strip and why has Israel declared war? - ABC News                                             | Sun, 08 Oct 2023 07:00:00 GMT | ABC News                             |
| 'The Middle East Region Is Quieter Today Than It Has Been in Two Decades' - The Atlantic                                                  | Sat, 07 Oct 2023 07:00:00 GMT | The Atlantic                         |
| MAP launches Gaza emergency response amid rapidly escalating violence - Medical Aid for Palestinians                                      | Sat, 07 Oct 2023 07:00:00 GMT | Medical Aid for Palestinians         |
| Video shows moment kidnapped woman begs Hamas fighters not to kill her - Business Insider                                                 | Sun, 08 Oct 2023 07:00:00 GMT | Business Insider                     |
| Israel-Gaza: More than 250 bodies found at site of Supernova festival - bbc.co.uk                                                         | Sat, 07 Oct 2023 07:00:00 GMT | bbc.co.uk                            |
| Just another battle or the Palestinian war of liberation? - The Electronic Intifada                                                       | Sun, 08 Oct 2023 07:00:00 GMT | The Electronic Intifada              |
| What is Israel's first line of defense, the Iron Dome? - Fox News                                                                         | Sun, 08 Oct 2023 07:00:00 GMT | Fox News                             |
| Israel-Hamas war: What to know about the attacks, casualties, hostages and the response - The Globe and Mail                              | Sun, 08 Oct 2023 07:00:00 GMT | The Globe and Mail                   |
| Terrifying video: Woman kidnapped on motorcycle to Gaza - Arutz Sheva                                                                     | Sat, 07 Oct 2023 07:00:00 GMT | Arutz Sheva                          |
| Articles, Videos and More IDF Updates: Hamas War on Israel (Oct 2023) - Announcements, Videos and More - idf.il                           | Sat, 07 Oct 2023 07:00:00 GMT | idf.il                               |
| DEVELOPING: 'Diplomatic sensitivities' prevented Israel from a retaliatory strike on Iran: Reports - News24                               | Sat, 07 Oct 2023 07:00:00 GMT | News24                               |

You should, therefore, focus more on scraping by timeframe than on a specific region. Getting the metadata of the news items such as title, publisher and date in JSON format is very easy, but scraping the underlying full-text items is a more challenging issue.

## The challenge of getting full-text behind the Google News links

The Google News scraping gives us a JSON file with basic metadata. However, this does not automatically give us the text content of the articles. The links that you get when interacting with the Google News site are not the actual links of the original news publishers but Google links that redirect to the original pages. When calling those links via script, you also have to find a way to let your machine accept cookies / terms and conditions before you can proceed. Visiting the weblinks as a human, you will see a pop-up asking you for confirmation. Without a confirmation, Google will not let you access the sources. This process thus needs to be automated for all scraped links. Running the code locally on your own computer gives you the possibility to manage this via a pre-set (Google Chrome) browser profile, but when you use the code (for teaching) in an environment like the Maastricht Data Science Research Infrastructure (DSRI), this is much more difficult to achieve. When we first worked with Google News scraping in 2023, we could successfully get the full-text content using the *newspaper3k* package within Anaconda environments on both Windows and MAC, but this solution did not function within DSRI. [*Newspaper3k*](https://newspaper.readthedocs.io/en/latest/) is a Python package for article scraping and curation. Compatible with Python3, it leverages lxml and it extracts articles from diverse web sources. Installation information: https://pypi.org/project/newspaper3k/

## Adjusting the code for different environments

To run the code in your own environment, e.g. your university's Jupyterlab, you need to change the first few lines of code relating to paths and package imports. On the Maastricht University DSRI, you need to import the relevant packages via <code>!pip install</code>, and it may also be necessary to define a specific output directory. 

If you are a member of an academic institution, consult with your ICT departments what's possible and how they can support you. If using bespoke packages like *newspaper3k* does not work in your particular coding environment, you may want to consider [decoding the scraped Google URLs to reconstruct the actual URLs](https://stackoverflow.com/questions/51131834/decoding-encoded-google-news-urls).

- option to get content directly from the websites: https://stackoverflow.com/questions/56829861/how-to-scrape-google-news-articles-content-from-google-news-rss
- this script has an option to scrape <code>article.text()</code> to CSV: https://github.com/pratikpv/google_news_scraper_and_sentiment_analyzer/blob/master/google_news_scraper.py

## Running code on Colab

It is also possible to run code in the easy-to-use Google Colab environment if you run into issues otherwise, but for academic settings, this is not recommended. Should you wish to access Google News via script in Google Colab, you also need to register your own Google API: 

https://github.com/topics/google-news-scraper
