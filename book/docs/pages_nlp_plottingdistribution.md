# Understanding and plotting probability distributions in NLP

## Definition of probability distribution

According to the Geeks for Geeks article [Fundamentals of statistics in natural language processing](https://www.geeksforgeeks.org/statistics-in-natural-language-processing/), a variety of statistical concepts and methods are used in NLP. One aspect are so-called *descriptive statistics*, which include frequency counts (e.g. represented in word clouds), measures of Central Tendency (mean, median, mode), and measures of dispersion (e.g. for analysing "variability in word or sentence lengths"). Another important statistical concept often used in NLP are so-called *probability distributions*. Probability distributions are used in NLP to model the natural variation and predictability of language.

Julia Hockenmaier, professor at the Siebel Center for Computer Science, University of Illinois, has outlined the most common probability models for NLP in [a lecture for the course CS447: Natural Language Processing](https://courses.grainger.illinois.edu/cs447/fa2020/Slides/Lecture03.pdf). This lecture introduces students of computer science and computational linguistics to how language models "define probability distributions over the strings in a language" (slide 5), explains n-gram models and outlines "some very basic probability theory". Slides 11 and 12 explain sampling with replacement (often covered in secondary school mathematics courses as well) and applies this process to a text as a "bag of words" (slide 13).

Slide 16 defines a probability distribution as frequently used in NLP. In natural language processing, a probability distribution assigns a value between 0 (0%) and 1 (100%) to each possible outcome. These outcomes are typically words or sequences of words. For example, NLP models trained on standard use of the English language assign a high probability to “the” following “of,” and a much lower probability to the word “banana.” This is also why you typically see decimal values below 1 when looking at statistical information in Voyant Tools. The space over which this distribution is defined is often called omega (Ω). This typically refers to all possible words or sentences within a language. 

### Discrete probability

Hockenmaier (slide 17) further introduces the concept of *discrete probability*, which refers to situations where there is a fixed number of possible outcomes. This is relevant to NLP because words are discrete units. A sentence consists of individual word tokens drawn from a known vocabulary. Inventing new words is possible but uncommon. The Bernoulli distribution is the simplest discrete probability distribution, defined over two outcomes, such as success/failure, yes/no, or true/false. While not unique to NLP, the Bernoulli distribution is frequently used when modelling binary decisions, such as whether a sentence ends or not. The categorical distribution is a generalisation of the Bernoulli: it describes the probability of one outcome from multiple categories. In NLP, this is used to model the probability of selecting a word from a vocabulary. These distributions allow language models to quantify uncertainty and variation in a structured way, based on observed data.

### Joint probability

*Joint probability* (Hockenmaier, slides 18–19) refers to the likelihood of two or more events occurring together. In the context of language, this could mean the probability of a word appearing in a certain position and another word appearing in relation to it: for instance, the probability of the phrase “war and peace.” The chain rule is a fundamental concept from probability theory that allows us to calculate the joint probability of a sequence of events (or words) by expressing it as a product of conditional probabilities. In practice, this means we break down the probability of a sentence into the probability of each word given the previous ones. For “war and peace”, this gives: P(war and peace) = P(war) × P(and | war) × P(peace | war and). The vertical bar is read as “given”, so P(and | war) is the probability of “and” following “war”.

However, calculating these probabilities can quickly become unmanageable due to the vast number of possible word combinations. This is why many language models make so-called independence assumptions. These assumptions simplify the model by pretending that certain parts of the language are independent — even if they aren’t in reality. This drastically reduces the number of parameters (probabilities) the model needs to estimate. It allows the model to be trained with less data, although at the cost of accuracy. These simplifications are common in statistical models, not just in NLP. Models in science never represent reality as is but present abstractions.

### Constructing efficient NLP models and limits of reliability

To build a useful probability model for language, two things are required: a model definition and parameter estimation. (Hockenmaier, slide 21) The model definition outlines the structure, for example, whether the model assumes each word depends on the last one or the last three. Parameter estimation refers to the process of calculating the actual probabilities from a dataset, usually based on how often certain word combinations appear in real texts. In practice, almost all language models make independence assumptions to make the model simpler and more trainable. Without them, the number of probabilities to estimate would be enormous, and we would never have enough training data to fill in all the necessary details. However, these assumptions are never perfect, and they lead to models that occasionally make unrealistic predictions — such as assigning high probabilities to ungrammatical or nonsensical sentences.

### n-gram models for word prediction

An n-gram model is a type of statistical language model used to predict the next word in a sequence. The “n” in n-gram refers to the number of words considered:

<blockquote>An n-gram language model assumes each word depends only on the last n−1 words.</blockquote> (Hockenmaier, slide 23) 

A bigram model (n=2) predicts each word based on the word that comes before it. A trigram model (n=3) considers the two previous words, and so on. In the example above, a bigram model would approximate P(peace | war and) by P(peace | and), simply ignoring “war”. This approach is a simplification of real language, which often depends on more than just the last few words. However, n-gram models are popular because they are relatively easy to train and interpret. They balance complexity with practicality: more context improves prediction, but too much context makes the model harder to manage.

### Approaching language from a mathematical perspective

It is important to remember that NLP depends on an abstract, mathematical approach to language. In these terms, a language model is a function that assigns probabilities to sequences of words. It tells us how likely it is that a particular sentence will occur. The model is trained on a vocabulary (meaning a fixed set of words) and can then be used to generate or analyze text. (Hockenmaier, slide 29)

The mathematical notation V* refers to all possible strings (sentences) that can be made from a vocabulary V. The model assigns probabilities to these strings, ideally in a way that reflects how people actually use language. One challenge is that we want a single model that works for strings of any length, not just for fixed-length sequences. This is where mathematical concepts like recursive probability estimation come in: we multiply the probabilities of each word given its history, and this allows us to generate or evaluate complete sentences.

### Beginning and End of Sentence Markers (BOS and EOS)

To train a language model effectively, we need to tell it where sentences begin and end. This is done by adding special tokens — BOS (beginning-of-sentence) and EOS (end-of-sentence) — to the training data. These markers are not real words but serve a crucial role: they let the model learn that language has structure, and that word choices often depend on the start and end of a sentence. (Hockenmaier, slide 32) By including these tokens, the model learns not only what words typically follow others, but also how sentences are shaped — where they tend to start and how they tend to conclude. For example, the sentence “Will you not tell me?” is stored as “BOS Will you not tell me EOS”, so the model can learn that “Will” is a likely first word and that a sentence can end after “me”.

### Maximum Likelihood Estimation (MLE)

A large amount of text is needed as training data to "learn" or "estimate" the parameters typical of a language and develop reliable probabilities. One of the simplest and most common ways to estimate probabilities in a language model is called *Maximum Likelihood Estimation* (MLE). This technique is not unique to NLP either as it is a core statistical method used in many fields. MLE works by using observed data to estimate how often each event occurs. In NLP, this usually means counting how often a word or phrase appears in a large corpus, and dividing that count by the total number of observations. The result is a probability: the likelihood that a given word will appear in a certain context. For instance, if “war” occurs 1,000 times in a corpus and is followed by “and” in 50 of these cases, MLE estimates P(and | war) = 50 / 1,000 = 0.05 (invented numbers for illustration). While MLE is easy to understand and implement, it does have limitations, especially when dealing with rare or unseen word combinations: a word pair that never occurs in the training data receives a probability of 0, which would make the probability of any sentence containing it 0 as well. More advanced models use smoothing techniques to handle this, but those are beyond the scope of this handbook. (Hockenmaier, slide 34)

### Generating Text with Language Models

As you will know from your own use of AI chatbots etc., language models are not only used for analyzing existing texts. They can also be used to generate new sentences. By sampling from a language model’s probability distributions, we can create strings of words that resemble natural language. Building grammatically correct strings is fairly easy, but selecting words that make sense to humans in combination requires advanced models and extensive training.

The examples given on Hockenmaier's slides do not necessarily make sense but show typical features of the text types chosen, e.g. frequently used vocabulary in a business journal or a Shakespeare work. Differences between adjectives, verbs, adverbs and nouns are not recognized to a sufficient degree, but the quadgram output is more logical than the unigram output that just puts individual words behind each other. A quadgram output includes grammatically correct sentences like "Will you not tell me who I am?".

The quality of the generated text, therefore, depends on the kind of model used, and the public accessibility of LLMs through tools like ChatGPT has made this very transparent in recent years. A unigram model (where each word is chosen independently) typically produces random word sequences with little structure. A quadgram model, on the other hand, uses more context and often produces much more coherent and grammatically correct output. This illustrates how important context is in language generation: the more of the sentence the model can "see," the more natural the output tends to be. (Hockenmaier, slide 39) Modern LLMs replace the counted probabilities of n-gram models with neural networks that can take much longer contexts into account, but they still work on the same principles of calculating a probability distribution and sampling from it.

### Evaluating Language Models

Finally, language models must be evaluated to understand how well they perform. There are two main approaches:

- Intrinsic evaluation looks at how well the model performs a specific task, such as predicting the next word in a sentence. A common intrinsic measure is perplexity, which expresses how "surprised" the model is by new text it has not seen during training (the lower, the better).

- Extrinsic evaluation measures how useful the model is in a larger system — for example, whether it improves the quality of a translation system or a search engine.

Evaluation is one of the most difficult parts of working with language models because human language is so flexible and nuanced. Different evaluation methods highlight different strengths and weaknesses in a model, and choosing the right method depends on the goals of your project. (Hockenmaier, slide 50)

## Making working with complex textual data easier by reduction

To make texts consisting of many different words easier to visualise, *dimensionality reduction* is applied. This technique reduces high-dimensional data (data with a lot of information) to representative core features so that we can understand it more easily. In NLP, you often find dimensionality reduction using the Principal Component Analysis (PCA) method (see section on scatterplots), which finds the most important features or directions in the data. It keeps as much of the original information as possible. In NLP, PCA takes high-dimensional word representations (embeddings, explained in the next section) and shows them in 2D or 3D plots so we can see patterns and relationships more clearly. t-SNE (t-Distributed Stochastic Neighbor Embedding) is another technique of dimension reduction, but it functions differently. It focuses on keeping similar items close together and is used for showing clusters of words or groups of documents in 2D or 3D. Note that only the closeness of points within a cluster is meaningful in a t-SNE plot: the distances between separate clusters and the size of the clusters should not be interpreted.

## Distributed representations / embeddings

In *distributed representations*, also known as *embeddings*, the idea is that the "meaning" or "semantic content" of a data point is distributed across multiple dimensions. Expressing it more simply, distributed representations or embeddings are a way of representing words as numbers. These numbers, or vectors, are like coordinates in a space where each word is a point. Words that have similar meanings are placed near each other in this space. For example, the words "cat" and "dog" might be close together because they are both animals, while "cat" and "car" might be farther apart, since they're not related in meaning. There are special techniques, like Word2Vec, GloVe, and FastText, that learn how to place words in this space by looking at lots of text. Real embeddings usually have hundreds of dimensions, which is why dimensionality reduction is needed to show them in a two-dimensional graph with an x- and a y-axis, with the different dots arranged between these axes. A plot like this is called a scatter plot.

## Reading scatter plots in general

To visalise probability distributions in NLP, scatter plots are common. In a scatter plot, the x-axis (horizontal) and y-axis (vertical) each represent a variable. Each dot drawn in a scatter plot corresponds to a unique observation in both dimensions. These dimensions can be absolute numbers, e.g. a person's age and income, or relative values, e.g. when we are considering word distributions in a text or a collection of texts. When points group together in a scatter plot, it suggests a concentration of data in that range. 

:chart_with_upwards_trend: If the points generally point upward (from bottom left to top right), it shows a positive correlation, meaning as one variable increases, the other increases, too. One example can be the relationship between study time and grades. If we find that students who study longer also have better grades in the exams, we speak of a positive correlation.

:chart_with_downwards_trend: A downward slope shows a negative correlation. One example of a negative correlation can be screen time versus sleep hours. As screen time increases, sleep tends to decrease as well.

If the points are scattered randomly with no clear slope or pattern, this indicates no statistical relationship between the variables. Keep in mind that a correlation shows that two variables change together, but not that one causes the other.

Some points may sit far away from the cluster, which could be outliers — unusual observations that differ significantly from the trend. These might signal unique cases or errors in data. For example, in a dataset of people's heights and weights, a person who is 1.80 m tall but was accidentally recorded as 18 meters in height would be an outlier caused by a data-entry error, whereas an exceptionally tall basketball player would be a genuine but unusual case.

Understanding scatter plots is not just about observing the dominant trend but about interpreting what the relationships of all points (or lack thereof) means. Ask questions like: “What could a strong positive correlation tell us about these two variables?”

## Uses of scatter plots in NLP

In NLP, scatter plots are commonly used to show relationships or similarities between words, sentences, or entire documents. Each point represents a word, sentence, or document based on its embedding or similarity score. In contrast to a scatter plot in which values such as age, income, height, weight, or length are measured, an NLP scatter plot can have negative values on both the x and y axes. These are not probabilities (which always lie between 0 and 1) but coordinates calculated by the dimensionality reduction method (see the above explanations based on Hockenmeier's slides). Most methods, such as PCA, centre the data on the average, so that the middle of the plot (0, 0) represents an average case. A negative value then simply means "below average" on that dimension, and a positive value "above average". Negative values therefore do not mean dissimilarity, and positive values do not mean similarity. The direction of an axis is also arbitrary and the same plot could be flipped without changing its meaning. What matters is the **distance between points**. Points that are close to each other share characteristics.

A non-NLP example of this is a PCA of the [Palmer Penguins dataset](https://gist.github.com/slopp/ce3b90b9168f2f921784de84fa445651), which is often used for teaching. It combines measurements such as bill length, flipper length and body mass of penguins into two new dimensions. You can see what this looks like in a PCA scatter plot somewhere in the middle of Allison Horst's visualisation notebook [PCA with penguins and recipes]([https://allisonhorst.github.io/palmerpenguins/articles/intro.html](https://allisonhorst.github.io/palmerpenguins/articles/pca.html). A penguin with a negative value on the first dimension is below average on the combination of measurements that this dimension summarises, and penguins of the Chinstrap species separate from the other two analysed species in this plot.

Depending on the context and the algorithms used, NLP scatter plots do not always represent the exact same values but can entail different properties, like two different sentiment scores (e.g., positive and negative) or dimensions of similarity. So be careful to check what exactly is being shown before you begin your analysis!

Special techniques, like Word2Vec, GloVe, and FastText, place words in the space based on their meanings, and the resulting vectors can be used to identify similar words, classify entire texts, or even translate languages. Some types of embeddings, like contextual embeddings (from models like BERT or GPT), do take the specific context into account, meaning each word has a unique embedding in each context. However, even in these cases, clustering will reflect shared meaning across contexts rather than specific occurrences within a particular text passage. Most scatter plots based on embeddings display nonlinear clusters if the embeddings capture complex, multidimensional meanings. Points far from clusters may represent unusual or ambiguous words, phrases, or sentences that do not fit into clear similarity groups. For example, highly context-dependent words or polysemous words (words with multiple meanings) might appear as outliers, indicating that they don’t neatly belong to a single cluster.

Voyant's scatter plot, however, work differently from embedding plots based on learned word meanings, so also read the dedicated Voyant section below.

## Understanding the scatter plot tool in Voyant

Unfortunately, the Voyant documentation for the scatter plot tool is quite abstract and short. It does not provide a lot of insight for beginners and uses many technical terms without definitions. According to this documentation, the Voyant scatter plots allow for several distribution techniques. 

The first one is **Principal Component Analysis (PCA)**, which "takes data in a multidimensional space and optimizes it, reducing the dimensions to a manageable subset. It is a way of transforming the data with respect to its own structure, so that associations between data points become more readily apparent." ([Scatterplot in the Voyant Tool Help](https://libvoyant.unm.edu/resources/voyant/current/docs/docs/index.html#!/guide/scatterplot)) Breaking this down, it is important to understand that a multidimensional space in data analysis is a way to describe data that has many different features. For example, each document in a collection might be considered one “dimension.” Too many dimensions make it hard to visualize patterns as you will see so many points in a chart that all the data overlap or that the scale becomes too small to read. This is why data need to be reduced and represented by fewer data points. Principal Component Analysis (PCA) is one such method that simplifies complex data by focussing on the biggest patterns in how things differ (variability / variance), so that they can be shown on a human-readable 2D or 3D plot. In Voyant, the data that are reduced are the term frequencies in the documents of your corpus. The tool therefore compares documents, so it works best with a corpus of several texts. A single long text can be split into segments first to use this tool meaningfully (see the section on segmentation).

In the example, I have uploaded three inaugural speeches by Trump, Obama and Biden (one each) to Voyant and performed PCA with 2 dimensions, 3 clusters, and 50 visible terms, which gave me the following chart:

<img width="1234" height="761" alt="image" src="https://github.com/user-attachments/assets/444fe2c9-f76d-4ad5-a3f9-7d69abe8afe2" />

First of all, it is important to understand that the colours here are assigned by the model based on the selected cluster count and are not intended to represent documents or speakers. Terms that lie far from the rest of a PCA plot are not necessarily the most interesting ones, so it is important to find out why they stand out. In my speech example, “america” is an outlier because it is both very frequent and distributed unevenly across the documents, and PCA is strongly influenced by such words. “Applause”, on the other hand, most likely stems from information about audience reactions in the transcripts rather than from the speakers’ language, which also makes this word behave differently.

**Correspondence Analysis (CA)** is the second distribution method that you can select in the Voyant scatter plots. It attempts data reduction similar to PCA, but it shows both words and documents in the same plot. You can thus see which words are typical of which documents. t

<img width="1234" height="754" alt="image" src="https://github.com/user-attachments/assets/9cc18337-b206-4ef3-bcd2-ceb399814e2c" />

My screenshot shows CA performed on the three presidential speeches by Trump, Biden and Obama with the terms count set to 25 and 3 dimensions. Again, the colours present model clusters, not speakers. However, we can now see the document names placed near words as well.

The third option in Voyant Tools scatter plots to analyse your document(s) is **t-SNE (t-Distributed Stochastic Neighbor Embedding)**, which also reduces high-dimensional data to a 2D or 3D plot, but it is non-linear and aims to preserve local neighbourhoods rather than the overall structure of the data. Terms or documents with similar distributions are therefore placed close together, which often produces clearer, more separated clusters than PCA or CA. The disadvantage is that closeness of points within a cluster is meaningful, while the distances between clusters, the size of clusters and the axis values should not be interpreted, and there is no percentage of explained variation. t-SNE is best used as an exploratory tool. 

**Document Similarity (DS)** is the last option and a variant of Correspondence Analysis that only shows documents (no words with labels). It shows which documents use language in statistically similar ways. As an example, I have put three inaugural speeches by three US presidents into Voyant Tools and received the following graph:

<img width="1228" height="752" alt="image" src="https://github.com/user-attachments/assets/1da05857-5ed5-4fc1-9b5c-2df1783d9bc0" />

At first glance, Obama and Biden look like a pair because they share the right-hand side, but the y-axis separates them almost as strongly as the x-axis separates Trump from both. Based on vocabulary, no pair of speeches is clearly more similar than the others. The near-even 54/46 split between the dimensions indicated in the top-left corner fits this since neither axis dominates.

### Options in the Voyant Tools scatter plots

The toolbar mainly comprises options for tweaking and exploring the plotting of the graph.

- *Analysis* allows the user to switch between plotting Document Similarity, Principal Component Analysis, t-Distributed Stochastic Neighbor Embedding, and Correspondence Analysis (see explanations in the section above).
- *Clusters* allows the user to control the number of groups to cluster the words into. These clusters are determined automatically by the criteria of the analysis and words in a cluster would indicate a measure of similarity between words. Clusters of terms will appear as a single colour.
- *Dimensions* allows the user to switch between two or three dimensions. 
- *Labels* allows the user to change the label settings for the graph.

### Terms

The Terms panel shows you which terms are displayed in the current scatterplot and it also allows you to control which terms are shown. The terms grid functions like other grids in Voyant and you can sort terms alphabetically or by frequency. The Terms panel also provides the following functionality:

- *Terms Count*: determine how many terms to display at once in the graph (the terms present will influence the layout of the terms, so it's well worth experimenting with this option)
- *Nearby*: you can select a term of interest from the grid and ask to zoom in on "nearby" terms (terms that cluster in proximity)
- *Remove*: you can remove one term at a time by selecting it in the grid and hitting the Remove button
- *Add Term*: you can search for and add new terms

### Reading the percentages and axes in the Voyant scatter plot

At the top of the plot, Voyant displays the line "Percentage of Total Association Explained by Each Dimension". In the example below, which shows a corpus of novels by Jane Austen, Dimension 1 (the x-axis) accounts for 33.16%, Dimension 2 (the y-axis) for 26.17% and Dimension 3 (shown as the fill of the points in this 2D view) for 23.49%.

:clipboard: insert screenshot of the Voyant scatter plot here

Each percentage tells you how much of the total variation in your data is captured by one dimension. In Correspondence Analysis, this variation is called *association*: it measures how much the documents differ in the words they favour, compared with a situation in which every document used every word in the same proportions (in which case there would be nothing to plot). In Principal Component Analysis, the same idea is usually called *variance*. Because the data have many more dimensions than a plot can show, the analysis calculates new dimensions, ordered from the most to the least informative, and the percentages show how the total is divided between them. They are therefore a measure of how complete the picture is, not of whether the results are correct or statistically significant.

In the example, the first two dimensions together explain 59.33% (33.16% + 26.17%) and all three 82.82%. This means that the flat plot leaves out about 41% of the differences between the texts, and about 17% is not shown in any form. Because the three values are fairly similar, no single dimension dominates, which is common with text data, and the third dimension is almost as important as the second. If the first two dimensions explained only a small share, the plot would be a poor summary: points that look close together might be far apart in the full data.

The numbers on the axes have no unit such as years or counts. They are coordinates relative to the centre (0, 0), which stands for the average distribution of words in the corpus. Terms near the centre, such as very frequent words that are used about equally in all novels, tell you little about the differences between the texts, which is why the centre of the example is so crowded and the labels overlap (adjusting the Terms Count and Labels options can help). The farther a term or a document is from the centre in a given direction, the more it differs from the average. Documents are shown as diamonds and terms as circles, and the size of a circle appears to reflect the frequency of the term. In the example, "sir" lies close to the Mansfield Park diamond and far from the other novels, which suggests that it is characteristic of that novel. Such a first impression should always be checked against the actual frequencies, for example in the Terms or Trends tool, because a plot that shows only part of the total variation can be misleading.

## Plotting from scratch with R and Python

If you want more control than Voyant offers, the same plots can be created with code. In R, `ggplot2` draws bar charts, histograms and scatter plots, `quanteda` (or `tidytext`) turns plain-text files into a document-term matrix, `prcomp()` runs PCA, `FactoMineR` and `factoextra` run and plot PCA and correspondence analysis, and `Rtsne` provides t-SNE. In Python, `pandas` and `scikit-learn` cover data preparation and analysis (`CountVectorizer` for the document-term matrix, `PCA` and `TSNE` for the reduction), `matplotlib`, `seaborn` and `plotly` draw the plots, `prince` offers correspondence analysis, and `gensim` or `sentence-transformers` provide embeddings. The data input depends on the plot. For probability distributions, including rank-frequency plots of word frequencies, you need a frequency table with one row per word (word, count, relative frequency). For Voyant-style scatter plots, you need a document-term matrix with one row per document (or text segment) and one column per term, filled with counts or relative frequencies. For embedding plots, you need a matrix with one row per word, sentence or document and hundreds of columns containing the vector values, produced by models such as Word2Vec, GloVe or BERT. Both languages can read plain-text files and CSV tables directly, for example an export from Voyant.

### Works cited and recommendations for further reading

Fundamentals of statistics in natural language processing (NLP). (2024, July 15). GeeksforGeeks. [https://www.geeksforgeeks.org/statistics-in-natural-language-processing](https://www.geeksforgeeks.org/statistics-in-natural-language-processing)

Hockenmaier, J. (2020). *Probability models for NLP* [Lecture slides]. CS447: Natural Language Processing, University of Illinois Urbana-Champaign. [https://courses.grainger.illinois.edu/cs447/fa2020/Slides/Lecture03.pdf](https://courses.grainger.illinois.edu/cs447/fa2020/Slides/Lecture03.pdf)

Sinclair, S., & Rockwell, G. (n.d.). ScatterPlot. In *Voyant Tools Help*. [https://voyant-tools.org/docs/#!/guide/scatterplot](https://voyant-tools.org/docs/#!/guide/scatterplot)
