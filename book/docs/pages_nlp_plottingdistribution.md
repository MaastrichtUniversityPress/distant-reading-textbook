# Understanding and plotting probability distributions in NLP

## Definition of probability distribution

According to the Geeks for Geeks article [Fundamentals of statistics in natural langauge processing](https://www.geeksforgeeks.org/statistics-in-natural-language-processing/), a variety of statistical concepts and methods are used in NLP. One aspect are so-called *descriptive statistics*, which include frequency counts (e.g. represented in word clouds), measures of Central Tendency (mean, median, mode), and measures of dispersion (e.g. for analysing "variability in word or sentence lengths"). Another important statistical concept often used in NLP are so-called *probability distributions*. Probability distributions are used in NLP to model the natural variation and predictability of language.

Julia Hockenmaier, lecturer at the Sibel Center, University of Illinois, has outlined the most common probability models for NLP in [a lecture for the course CS447: Natural Language Processing](https://courses.grainger.illinois.edu/cs447/fa2020/Slides/Lecture03.pdf). This lecture introduces students of computer science and computational linguistics to how language models "define probability distributions over the strings in a language" (slide 5), explains n-gram models and outlines "some very basic probability theory". Slides 11 and 12 explain sampling with replacement (often covered in secondary school mathematics courses as well) and applies this process to a text as a "bag of words" (slide 13).

Slide 16 defines a probability distribution as frequently used in NLP. In natural language processing, we often work with probability distributions to describe how likely different outcomes are. A probability distribution assigns a value between 0 (0%) and 1 (100%) to each possible outcome. In language modelling, these outcomes are typically words or sequences of words. For example, NLP models, trained on typical language use, assign a high probability to “the” following “of,” and a lower probability to the word “banana.” This is also why you typically see decimal values below 1 when looking at statistical information in Voyant Tools. The space over which this distribution is defined is often called omega (Ω). This typically refers to all possible words or sentences within a language. 

### Discrete probability

Hockenmaier (slide 17) further introduces the concept of discrete probability, which refers to situations where there is a fixed number of possible outcomes. This is relevant to NLP because words are discrete units. A sentence consists of individual word tokens drawn from a known vocabulary. Inventing new words is possible but uncommon. The Bernoulli distribution is the simplest discrete probability distribution, defined over two outcomes, such as success/failure, yes/no, or true/false. While not unique to NLP, the Bernoulli distribution is frequently used when modelling binary decisions, such as whether a sentence ends or not. The categorical distribution is a generalisation of the Bernoulli: it describes the probability of one outcome from multiple categories. In NLP, this is used to model the probability of selecting a word from a vocabulary. These distributions allow language models to quantify uncertainty and variation in a structured way, based on observed data.

### Joint probability

Joint probability (Hockenmaier, slides 18–19) refers to the likelihood of two or more events occurring together. In the context of language, this could mean the probability of a word appearing in a certain position and another word appearing in relation to it: for instance, the probability of the phrase “war and peace.” The chain rule is a fundamental concept from probability theory that allows us to calculate the joint probability of a sequence of events (or words) by expressing it as a product of conditional probabilities. In practice, this means we break down the probability of a sentence into the probability of each word given the previous ones.

However, calculating these probabilities can quickly become unmanageable due to the vast number of possible word combinations. This is why many language models make so-called independence assumptions. These assumptions simplify the model by pretending that certain parts of the language are independent — even if they aren’t in reality. This drastically reduces the number of parameters (probabilities) the model needs to estimate. It allows the model to be trained with less data, although at the cost of accuracy. These simplifications are common in statistical models, not just in NLP.

### Constructing efficient NLP models and limits of reliability

To build a useful probability model for language, two things are required: a model definition and parameter estimation. (Hockenmaier, slide 21) The model definition outlines the structure, for example, whether the model assumes each word depends on the last one or the last three. Parameter estimation refers to the process of calculating the actual probabilities from a dataset, usually based on how often certain word combinations appear in real texts. In practice, almost all language models make independence assumptions to make the model simpler and more trainable. Without them, the number of probabilities to estimate would be enormous, and we would never have enough training data to fill in all the necessary details. However, these assumptions are never perfect, and they lead to models that occasionally make unrealistic predictions — such as assigning high probabilities to ungrammatical or nonsensical sentences.

### n-gram models for word prediction

An n-gram model is a type of statistical language model used to predict the next word in a sequence. The “n” in n-gram refers to the number of words considered:

<blockquote>An n-gram language model assumes each word epends only on the last n−1 words.</blockquote> (Hockenmaier, slide 23) 

A bigram model (n=2) predicts each word based on the word that comes before it. A trigram model (n=3) considers the two previous words, and so on. This approach is a simplification of real language, which often depends on more than just the last few words. However, n-gram models are popular because they are relatively easy to train and interpret. They balance complexity with practicality: more context improves prediction, but too much context makes the model harder to manage.

### Approaching language from a mathematical perspective

It is important to remember that NLP depends on an abstract, mathematical approach to language. In these terms, a language model is a function that assigns probabilities to sequences of words. It tells us how likely it is that a particular sentence will occur. The model is trained on a vocabulary (meaning a fixed set of words) and can then be used to generate or analyze text. (Hockenmaier, slide 29)

The mathematical notation V* refers to all possible strings (sentences) that can be made from a vocabulary V. The model assigns probabilities to these strings, ideally in a way that reflects how people actually use language. One challenge is that we want a single model that works for strings of any length, not just for fixed-length sequences. This is where mathematical concepts like recursive probability estimation come in: we multiply the probabilities of each word given its history, and this allows us to generate or evaluate complete sentences.

### Beginning and End of Sentence Markers (BOS and EOS)

To train a language model effectively, we need to tell it where sentences begin and end. This is done by adding special tokens — BOS (beginning-of-sentence) and EOS (end-of-sentence) — to the training data. These markers are not real words but serve a crucial role: they let the model learn that language has structure, and that word choices often depend on the start and end of a sentence. (Hockenmaier, slide 32) By including these tokens, the model learns not only what words typically follow others, but also how sentences are shaped — where they tend to start and how they tend to conclude.

### Maximum Likelihood Estimation (MLE)

A large amount of text is needed as training data to "learn" or "estimate" the parameters typical of a language model and develop reliable probabilities. 
One of the simplest and most common ways to estimate probabilities in a language model is called Maximum Likelihood Estimation, or MLE. This technique is not unique to NLP — it is a core statistical method used in many fields. MLE works by using observed data to estimate how often each event occurs. In NLP, this usually means counting how often a word or phrase appears in a large corpus, and dividing that count by the total number of observations. The result is a probability: the likelihood that a given word will appear in a certain context. While MLE is easy to understand and implement, it does have limitations, especially when dealing with rare or unseen word combinations. More advanced models use smoothing techniques to handle this, but those are beyond the scope of this course. (Hockenmaier, slide 34)

### Generating Text with Language Models

As you will know from your own use of AI chatbots etc., language models are not only used for analyzing existing texts — they can also be used to generate new sentences. By sampling from the model’s probability distributions, we can create strings of words that resemble natural language. Building grammatically correct strings is fairly easy, but selecting words that make sense to humans in combination requires advanced models and extensive training.

The examples given on Hockenmaier's slides do not necessarily make sense but show typical features of the text types chosen, e.g. frequently used vocabulary in a business journal or a Shakespeare work. Differences between adjectives, verbs, adverbs and nouns are not recognized to a sufficient degree, but the quadrigram output is more logical than the unigram output that just puts individual words behind each other. A quadigram output includes grammatically correct sentences like "Will you not tell me who I am?".

The quality of the generated text, therefore, depends on the kind of model used, and the public accessibility of LLMs through tools like ChatGPT has made this very transparent in recent years. A unigram model (where each word is chosen independently) typically produces random word sequences with little structure. A quadgram model, on the other hand, uses more context and often produces much more coherent and grammatically correct output. This illustrates how important context is in language generation: the more of the sentence the model can "see," the more natural the output tends to be. (Hockenmaier, slide 39)

### Evaluating Language Models

Finally, language models must be evaluated to understand how well they perform. There are two main approaches:

- Intrinsic evaluation looks at how well the model performs a specific task, such as predicting the next word in a sentence.

- Extrinsic evaluation measures how useful the model is in a larger system — for example, whether it improves the quality of a translation system or a search engine.

Evaluation is one of the most difficult parts of working with language models because human language is so flexible and nuanced. Different evaluation methods highlight different strengths and weaknesses in a model, and choosing the right method depends on the goals of your project. (Hockenmaier, slide 50)

## Making working with complex textual data easier by reduction

To make texts consisting in many different words easier to visualise, *dimensionality reduction* is applied. This technique reduces high-dimensional data (data with a lot of information) to representative core features so that we can understand it more easily. In NLP, you often find dimensionality reduction using the Principal Component Analysis (PCA) method (see section on scatterplots), which finds the most important features or directions in the data. It keeps as much of the original information as possible. In NLP, PCA takes high-dimensional word representations (embeddings) and shows them in 2D or 3D plots so we can see patterns and relationships more clearly. t-SNE (t-Distributed Stochastic Neighbor Embedding) is another technique of dimension reduction, but it functions differently and creates semantic distributions. It focuses on keeping similar items close together. It is used for showing clusters of words or groups of documents in 2D or 3D.

## Distributed representations / embeddings

In *distributed representations*, also known as *embeddings*, the idea is that the "meaning" or "semantic content" of a data point is distributed across multiple dimensions. Expressing it more simply, distributed representations or embeddings are a way of representing words as numbers. These numbers, or vectors, are like coordinates in a space where each word is a point. Words that have similar meanings are placed near each other in this space. For example, the words "cat" and "dog" might be close together because they are both animals, while "cat" and "car" might be farther apart, since they're not related in meaning. There are special techniques, like Word2Vec, GloVe, and FastText, that learn how to place words in this space by looking at lots of text. The space can be a two-dimensional graph with an x- and a y-axes, with the different dots arranged between these axes. A plot like this is called a scatter plot.

## Reading scatter plots

In a scatter plot, the x-axis (horizontal) and y-axis (vertical) each represent a variable. Each dot drawn in a scatter plot corresponds to a unique observation in both dimensions. These dimensions can be absolute numbers, e.g. a person's age and income, or relative values, e.g. when we are considering word distrubitions in a text or a collection of texts. When points group together in a scatter plot, it suggests a concentration of data in that range. 

:chart_with_upwards_trend: If the points generally point upward (from bottom left to top right), it shows a positive correlation, meaning as one variable increases, the other increases, too. One example can be the relationship between study time and grades. If we find that students who study longer also have better grades in the exams, we speak of a positive correlation.

:chart_with_downwards_trend: A downward slope shows a negative correlation. One example of a negative correlation can be screen time versus sleep hours. As screen time increases, sleep tends to decrease as well.

If the points are scattered randomly with no clear slope or pattern, this indicates no relationship between the variables.

:chart_with_upwards_trend: add sample graph for number of pets and student grades

Some points may sit far away from the cluster, which could be outliers — unusual observations that differ significantly from the trend. These might signal unique cases or errors in data.

:clipboard: find non-NLP example

Understanding scatter plots is not just about observing the dominant trend but about interpreting what the relationships of all points (or lack thereof) means. Ask questions like: “What could a strong positive correlation tell us about these two variables?”

In NLP, scatter plots are commonly used to show relationships or similarities between words, sentences, or entire documents. Each point represents a word, sentence, or document based on its embedding or similarity score. In contrast to a scatter plot in which values such as age, income, height, weight, or length are measured, an NLP scatter plot can have negative values on both the x and y axes because we deal with probability measures. Negative values represent dissimilarity where positive values express similarity.

:clipboard: find non-NLP example based on data used for teaching

Depending on the context and the algorithms used, NLP scatter plots do not always represent the exact same values but can entail very different properties, like two different sentiment scores (e.g., positive and negative) or dimensions of similarity. So be carefuly to check what exactly is being shown before you begin your analysis!

In NLP scatter plots, clustering often indicates semantic similarity rather than direct co-occurrence in the text or corpus itself. The distance between points can then signal semantic similarity (closer points mean more similar meaning or sentiment). For example, "doctor" and "nurse" or "master" and "slave" might cluster together due to shared contexts in training data, but they don’t necessarily appear together in the text. 

:clipboard: add example using Voyant

This is why NLP scatter plots are similar to mind maps or conceptual maps rather than a structured representation of the text. Some algorithms may also result in point / words clusters in which words behave similarly in statistical terms while there is no content-based relationship between them. 

:clipboard: add example chart

Moreover, scatter plots in NLP sometimes reveal linear trends if there’s a direct relationship between two similarity measures, but more often display nonlinear clusters if embeddings capture complex, multidimensional meanings. Points far from clusters may represent unusual or ambiguous words, phrases, or sentences that do not fit into clear similarity groups. For example, highly context-dependent words or polysemous words (words with multiple meanings) might appear as outliers, indicating that they don’t neatly belong to a single cluster.

Special techniques, like Word2Vec, GloVe, and FastText, place words in the plot placed on word meanings and identify similar words, classify entire texts, or even translating languages. Some types of embeddings, like contextual embeddings (from models like BERT or GPT), do take the specific context into account, meaning each word has a unique embedding in each context. However, even in these cases, clustering will reflect shared meaning across contexts rather than specific occurrences within a particular text passage.

## Understanding the scatter plot tool in Voyant

Unfortunately, the Voyant documentation for the scatter plot tool is quite abstract and short. It does not providing a lot of insight for beginners and uses many technical terms without definitions. According to this documentation, the Voyant scatter plots allow for several distribution techniques. 

The first one is **Principal Component Analysis (PCA)**, which "takes data in a multidimensional space and optimizes it, reducing the dimensions to a manageable subset. It is a way of transforming the data with respect to its own structure, so that associations between data points become more readily apparent." (Voyant Documentation)

Breaking this down, it is important to understand that a multidimensional space in data analysis is a way to describe data that has many different features. For example, each document in a collection might be considered one “dimension.” Too many dimensions make it hard to visualize patterns as you will see so many points in a chart that all the data overlap or that the scale becomes too small to read. This is why data need to be reduced and represented by fewer data points. Principal Component Analysis (PCA) is one such method that simplifies complex data by focussing on the biggest patterns in how things differ (variability / variance), so that they can be shown on a human-readable 2D or 3D plot.

**Correspondence Analysis (CA)** is another distribution method that you can select in the Voyant scatter plats. It attempts data reduction similar to PCA, but it shows both words and documents in the same plot. You can thus see which words are typical of which documents. **Document Similarity (DS)** is a variant of Correspondence Analysis that only shows documents (no word labels). It shows which documents use language in statistically similar ways.

### Options in the Voyant Tools scatter plots

The toolbar mainly comprises options for tweaking and exploring the plotting of the graph.

- *Analysis* allows the user to switch between plotting Document Similarity, Principal Component Analysis and Correspondence Analysis (see explanations in the section above)
- *Clusters* allows the user to control the number of groups to cluster the words into. These clusters are determined automatically by the criteria of the analysis and words in a cluster would indicate a measure of similarity between words. Clusters of terms will appear as a single colour.
- *Dimensions* allows the user to switch between two or three dimensions. 
- *Labels* allows the user to cycle through the label settings for the graph.

### Terms

The Terms panel shows you which terms are displayed in the current scatterplot and it also allows you to control which terms are shown. The terms grid functions like other grids in Voyant and you can sort terms alphabetically or by frequency. The Terms panel also provides the following functionality:

- *Terms Count*: determine how many terms to display at once in the graph (the terms present will influence the layout of the terms, so it's well worth experimenting with this option)
- *Nearby*: you can select a term of interest from the grid and ask to zoom in on "nearby" terms (terms that cluster in proximity)
- *Remove*: you can remove one term at a time by selecting it in the grid and hitting the Remove button
- *Add Term*: you can search for and add new terms

:hammer_and_wrench: Under construction

### Works cited and recommendations for further reading

Fundamentals of statistics in natural language processing(Nlp). (2024, July 15). GeeksforGeeks. [https://www.geeksforgeeks.org/statistics-in-natural-language-processing](https://www.geeksforgeeks.org/statistics-in-natural-language-processing)

Recommended lecture on [Probability Models for NLP](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://courses.grainger.illinois.edu/cs447/fa2020/Slides/Lecture03.pdf&ved=2ahUKEwibh46n28yJAxXx9bsIHauuDNkQFnoECBMQAQ&usg=AOvVaw2q5YGp2ei5kG-8cN3PGHY5)