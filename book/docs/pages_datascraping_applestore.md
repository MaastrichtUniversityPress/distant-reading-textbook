# Data scraping from the Apple Store

## Working with Apple Store reviews in research

Podcast reviews provide an interesting source of user-generated content that can help us understand the tastes and opinions of different audiences. This can be relevant for product evaluation and marketing, but also for academic research in media studies, cultural studies, politics, gender studies, etc. Podcast reviews typically cover emotional responses and personal experiences as well as critical reflections. They can give insight into prevailing stereotypes and fears, but also in people's argumentations and knowledge.

## How to collect podcast reviews from the Apple Store

For scraping the podcast reviews from the [Apple Store](https://www.apple.com/apple-podcasts/), we will use a [Python](https://www.python.org/doc/essays/blurb/) script. In the past, we had to update the script several times to use different scraping packages as older packages caused API errors and were no longer maintained by their developers. According to the official website, "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics." You will **not** need to understand the details of programming to run Python code in the [UM DSRI](https://dsri.maastrichtuniversity.nl/). But you will need to know which variables in the code to change for the required output.

In the academic year of 2022/2023, Monika Barget started experimenting with code for downloading podcast reviews because one of the MA DC thesis students was interested in analyzing *True Crime* podcast reviews via distant reading. The Apple podcast reviews turned out to be an exciting source because they are normally rich in content and relatively easy to scrape. The HTML of the Apple Store site is well-structured, and some developers have already built specialized Python packages (collections of code) to harvest them. The package we used in 2023, [App Store Scraper](https://pypi.org/project/app-store-scraper/) for Apple, which was originally developed by Eric Lim under an MIT License (MIT), is unfortunately no longer working.

The Python scripts for the App Store provided in the code section of this repository now make use of a different scraping package and will be updated again if necessary.

To scrape reviews for a particular podcast, scripts generally need the following information:

- country of podcast
- name of podcast
- official app ID
- number of reviews to be scraped

You will always find the podcast name, the country code, and the app ID in the podcast URL.

Example: [https://podcasts.apple.com/us/podcast/black-girl-gone-a-true-crime-podcast/id1556267741?see-all=reviews](https://podcasts.apple.com/us/podcast/black-girl-gone-a-true-crime-podcast/id1556267741?see-all=reviews)

In the actual script, the information will be structured like this:

```python
app_id = 437299706
app_name = 'last-podcast-on-the-left'
country = 'us'
```
To maximise the number of reviews we can collect per podcast, the scripts provided in this repository employ multi-threading by default to scrape all available country codes. If you would like to reduce the number of countries from which you collect data beforehand, you will need to update the separate country code list read by the script. Please check the instructions within the relevant Jupyter notebook for details.

## Output data and how they can be analysed

The reviews which we can collect via the Apple API include the star-ratings, dates, and reviewer names. 
All the information is written into a table format and saved as a CSV file for further processing. 
CSV files can easily be imported into Open Refine (see additional instructions) for data filtering.
This allows you, for instance, to understand how often certain ratings occur, or when people have left the most reviews.
You can also export the comments as text information and further analyse them using Voyant Tools.

The following YouTube video by Monika explains the process of filtering data in Open Refine and exporting them step-by-step:

[![Thumbnail](https://img.youtube.com/vi/oMWIUf5_9jM/maxresdefault.jpg)](https://youtu.be/oMWIUf5_9jM?si=ibxc2zxcn335uGOo)

The focus is on using a general text filter to find keywords and using the facet filter to explore rankings. However, OpenRefine has many other
exciting functionalities not covered in this brief introduction! If you want to learn more, check out other videos shared by researchers and librarians on YouTube. One [Open Refine tutorial provided by researchers from Edinburgh](https://www.youtube.com/watch?v=wfS1qTKFQoI) does not only explain editing spreadsheets but also covers uploading data easily to Wikidata, which may be of interest to you in the future.
