# Distant reading case study "True Crime"

🙌 This case study was inspired by my MA student Nicole Schanzmeyer who wrote her thesis on this topic in the academic year of 2022/2023.

## The cultural relevance of True Crime podcasts

**True crime** is one of the most popular media genres of the digital age (Richards, 2023). Its popularity can be attributed to a captivating blend of mystery, suspense, real-world drama and, in many cases, troubling insights into subcultures, politics, and police work. It taps into our fascination with the darker aspects of human nature, providing a window into the minds of both criminals and investigators. Analysing true crime podcast reviews via distant reading offers a unique opportunity to better understand why listeners tune in and what they like about their favourite shows, but also what they think should be improved. By employing computational tools to sift through countless reviews, we can identify recurring themes and patterns that we might overlook in a close reading approach.

For your first distant reading experiments, we would like you to work with a relatively small datasets of [reviews](https://raw.githubusercontent.com/MonikaBarget/distant-reading/tree/main/data/Webscraping_samplePodcastReviews/Serial-1-and-2-stars-sub-corpus-csv.txt) on the successful American true crime podcast [Serial](https://podcasts.apple.com/us/podcast/serial/id917918570) (Reed et al., 2014–present). All the reviews selected for the dataset have 1 or 2 star ratings, so listeners who left the reviews obviously did not like it all that much. The dataset only contains the reviews and does not give you any indication who posted them when. To find that out, you can consult the [full data set in CSV format](https://github.com/MonikaBarget/distant-reading/blob/main/data/Webscraping_samplePodcastReviews/Serial_1-and-2-stars_sub-corpus.csv).

## Ingest your data into Voyant Tools

Go the the [Voyant Tools](https://voyant-tools.org/) website and simply paste the URL of the data (as indicated in the link above) into the "add text" field. Press the blue "reveal" button and start exploring the data set!

## Tasks to perform in Voyant

### High-level analysis with word cloud and frequencies table

- Look at the word cloud and the corresponding frequencies table. What words are the most prominent? What different topics or themes can you identitfy in the data?
- Who are the "protagonists" mentioned in the data? Are any people mentioned by name and who are they? Show hosts, politicians, police officers?
- What places (e.g. cities) are mentioned in the data? Why do you think that could be the case?
- What surprises you? What information is hard to contextualise?

### Comparative analysis with the "trends" tool

- Write down words that express emotions / people's feelings towards the show and its hosts. Put them into the trends tool. How did these emotions develop over time?
- Try to find groups of words for comparative analysis in "trends". This group of words has to be homogenous. You can, for example, look at different place names or trace the trends for different adjectives (e.g. "good", "bad", "exciting", "boring"). It does not make sense to combine terms from different word groups.

### Analysing co-occurences in the terms berry and other "links" tools

- What words are most prominently associated with the words "police" and "cop"? What does this say about the listeners' opinions?
- Try other words such as "criminals", "journalism" or "investigators". What are the results? What do they tell us about the podcast and perhaps also about more general debates in the United States?

### Reading keywords in context

- Put the words which you have used to find co-occurences in the "context" tool to see the full sentences in which they are used. Does this give you any additional insights?

### Drawing general conclusions

- What conclusions can you draw from all the individual distant reading results?
- What is (un)expected?
- What would have been difficult to find via close reading?
- What research questions would be interesting to explore based on this data set?

### Cited Works and Further Readings

- Fathallah, J. (2022). ‘Being a fangirl of a serial killer is not OK’: Gatekeeping Reddit’s true crime community. *New Media & Society, 26*(10), 5638–5657. https://doi.org/10.1177/14614448221138768
- Linke, C., & Brune, L. (2025). Intimate yet exploitative: Representations of gender-based violence in platformed true crime narratives. *Media and Communication, 13.* https://doi.org/10.17645/mac.8964
- Peters, F. (2020). True crime narratives. *Crime Fiction Studies, 1*(1), 23–40. https://doi.org/10.3366/cfs.2020.0005
- Reed, B., Chace, Z., Joffe-Walt, C., Syed, H., Updike, N., & Koenig, S. (Hosts). (2014–present). *Serial* [Audio podcast]. Serial Productions & The New York Times. https://podcasts.apple.com/us/podcast/serial/id917918570
- Richards, E. (2023, July 17). *True crime: Insight into the human fascination with the who-done-it.* Social Science Space. https://www.socialsciencespace.com/2023/07/true-crime-insight-into-the-human-fascination-with-the-who-done-it/
- Sherrill, L. A. (2020). The “Serial Effect” and the true crime podcast ecosystem. *Journalism Practice, 16*(7), 1473–1494. https://doi.org/10.1080/17512786.2020.1852884
