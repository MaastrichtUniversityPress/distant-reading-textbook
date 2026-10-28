# Sentiment Analysis

## What is Sentiment Analysis?

Sentiment analysis is the computational process of identifying and quantifying subjective information, such as opinions, emotions, and attitudes—from text data. It is widely used in natural language processing (NLP) to determine whether a piece of writing is positive, negative, or neutral. By analysing language patterns, sentiment analysis helps businesses, researchers, and organizations understand public perception, customer feedback, or social media trends. For example, companies often use sentiment analysis to evaluate customer satisfaction from product reviews or social media comments. (Moreno & Iglesias, 2020) Similarly, Kerstin Denecke (2023) has shown how sentiment analysis can help identify "sentiments or emotions expressed in free-textual documents with a scope on healthcare and medicine." However, the automated classifications of words can be difficult as it is highly context-depending. The same word can mean something else entirely when used in a different sentence, so merely rule-based / dictionary-based classifications tend to be misleading. Advances in Machine Learning now offer opportunities for more complex, contextual sentiment analysis, and tools or software packages trained for a particular domain often perform better than general applications. (Pozzi et al., 2017)

## Sentiment Analysis in Voyant Tools

Voyant Tools offers features for sentiment analysis through automated tagging of words, particularly adjectives, with positive or negative connotations. This process involves assigning sentiment scores to words based on predefined lexicons. However, the automated tagging in Voyant Tools often requires fine-tuning to ensure meaningful analysis as the word "like" is highlighted as positive by default while "miss" is flagged as negative. Both words, however, can have different meanings. "Like" is a verb, but can also be used in comparisons, and "miss" can be a term to address a young / unmarried woman. (See Voyant Tool's own documentation for a relevant screenshot: [https://voyant-tools.org/docs/tutorial-categories.html](https://voyant-tools.org/docs/tutorial-categories.html)) Without careful adjustment, the results may include false positives or misclassifications.

In addition to Voyant's @positive and @negative classifications of words, the categories dropdown now includes additional options, many of which are not related to sentiment but appear to be based on the [Harvard General Inquirer dictionaries](https://inquirer.sites.fas.harvard.edu/homecat.htm). These dictionaries group words into semantic and functional classes, such as social roles. Once a new category is selected, its terms are highlighted in the *Terms* tool, each category in its own colour. Searching for a category returns the combined frequency of all its words, and categories can also be plotted in *Trends* and compared with other categories or with individual terms. Users can edit existing categories or create their own in the category editor. Here, too, it is important to be careful and transparent as these categories are based on fixed word lists and do not provide a flexible analysis of meaning.

## Other Tools for Sentiment Analysis

Beyond Voyant Tools, there are numerous platforms and programming libraries designed for sentiment analysis.
Code-based tools for sentiment analysis include [TextBlob](https://www.geeksforgeeks.org/python/python-textblob-sentiment-method/) in Python and provide access to pre-trained models and lexicons.
A sentiment analysis tool with a graphic user interface to be run in browsers is Bert XY’s [SENSOR (SentimEnt aNalysiS Of Reviews)](https://procodiszuyd.eu.pythonanywhere.com/SENSOR_input/) platform
designed at Hoge School Zuyd to introduce students to sentiment analysis, focusing on customer reviews. 
The tool allows users to input review data and automatically analyzes the sentiment by tagging words — primarily adjectives — with positive or negative connotations. 
This process is based on predefined sentiment lexica, which classify words according to their emotional tone. The platform is intentionally kept simple to highlight both the potential and the limitations of automated sentiment analysis. Students are encouraged to critically assess the results, identify inaccuracies, and consider how the analysis could be improved. The tool also includes supplementary resources to guide students through the process.

### Resources

Denecke, K. (2023). Sentiment analysis in the medical domain. Springer. https://doi.org/10.1007/978-3-031-30187-2

Moreno, A., & Iglesias, C. A. (2020). Sentiment Analysis for Social Media. MDPI - Multidisciplinary Digital Publishing Institute.

Pozzi, F. A., Fersini, E., Messina, E., & Liu, B. (2017). Sentiment analysis in social networks. Morgan Kaufmann. https://search.ebscohost.com/login.aspx?direct=true&scope=site&db=nlebk&db=nlabk&AN=1144691
