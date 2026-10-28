# Strategies of text segmentation for (comparative) distant reading

## Why segmentation

According to the [Hyperscience knowledge base](https://www.hyperscience.com/knowledge-base/natural-language-processing/), "segmentation in NLP involves breaking down a larger piece of text into smaller, meaningful units such as sentences or paragraphs." This can allow a more systematic comparison across several clearly defined sections of text. In my classes, I usually refer to segmentating text into larger units as my students do not perform advanced linguistic analysis.

However, many NLP tasks depend on segmentation at a much smaller scale. One example is given in Tumi Moeng, Sheldon Reay, Aaron Daniels, and Jan Buys's work on the Southern African Nguni language group. Their focus is morphological segmentation, which "involves decomposing words into morphemes, the smallest meaning-bearing units of language." (Moeng et al., 2021) This process is important in the analysis of agglutinative languages such as the Nguni languages because a single written word can combine many morphemes that together express what English needs a whole sentence for. Counting such words as whole units produces very sparse and misleading frequencies, since most forms appear only once. Splitting them into morphemes gives tools like automated taggers, translators and search engines a more reliable training basis.

Segmentation also matters for the advanced language models behind many new AI-powered tools for language processing. The automated splitting of texts into tokens ([words or sub-words in the context of natural language processing](https://www.geeksforgeeks.org/nlp/nlp-how-tokenizing-text-sentence-words-works/)) is often only optimised for widely used languages such as English. In historical Hebrew, the clitic *dalet* is attached to the following word and has two grammatical functions (subordinating conjunction and possessive preposition). Because the two look identical on the page, ordinary processing can’t distinguish them. Rachel Tal, Cheyn Shmuel Shmidman and Avi Shmidman, therefore, built a BERT model in which all prefixes are split off and encoded as separate tokens, so the model can evaluate the clitic directly. (Tal et al., 2026)

## Structural approaches

### Author- or publisher-defined segmentation

A structural approach to segmentation is to divide a text into sections that are already predefined by the author or publisher. This can be, for instance, volumes or chapters. You can also separate an appendix from the main text, or treat references or endnotes separately.

### Fixed-size segmentation

A purely quantitative alternative is to split a text into segments of equal length, for example 1,000 words each. This makes the segments directly comparable in size and is the approach that several tools in the Voyant Tools suite, such as Trends and Bubblelines, take by default. The disadvantage is that the cuts ignore the structure of the text, so a segment may begin or end in the middle of a scene or chapter and even divide sentences.

## Alternative segmentation approaches

More complex, content-related segmentations are also possible and can help you gain additional insights into a text, especially when it has several narrative layers.

### Introduction, main section, ending

One approach can be to treat the introduction (if there is one) as one separate section and to also split the ending or conclusion from the rest of the text, assuming that the introduction sets the stage for what happens after and that the conclusion offers some form of resolution. This can be especially interesting when you expect a plot twist or a major change in tone, e.g. in a crime novel.

### Dividing the main plot from one or more sub-plots

Dividing the main plot from one or more sub-plots can help you explore differences in tone and character description between these sections. This is especially interesting when a sub-plot (in a literary work) is used to offer a different world view than the main plot. One example of a novel with contrasting main and sub plots is [Anna Karenina](https://www.gutenberg.org/ebooks/1399).

### Dividing text by setting or location

If your text has different settings or locations, this can be another interesting division marker and can help you explore differences in the description of spaces and the people moving within them. In the novel [Dracula](https://www.gutenberg.org/ebooks/345), for instance, you could seperate sections playing out in Dracula's castle from sections set on the ship, in the asylum, or in the houses of the different characters.

### Segmentation by narrator or narrative level

Some texts contain several narrators or are nested in narrative frames. Segmenting by narrator lets you compare how each voice tells its story, which is different from segmenting by character, because it follows who is telling the story rather than who it is about.

### Segmentation by time

If your text contains flashbacks, time jumps or diary entries, you can divide it by chronological period or by the difference between story time and narrated time. This helps you explore how language and tone shift between the present of the narration and the events it recounts. In Wuthering Heights, for instance, you could separate the frame narrative from the events Nelly Dean recounts from the past.

### Segmentation based on central characters

In texts whose sections focus clearly on different (groups of) characters, creating segments dedicated to these individual characters is another option. This segmentation strategy is especially recommended for texts that offer point-of-view narratives, such as in the [A Song of Ice and Fire](https://en.wikipedia.org/wiki/A_Song_of_Ice_and_Fire) fantasy series.

### Segmentation by speech type

If your text includes narrated text as well as direct speech, you may want to use segmentation to separate them for a comparative analysis.

### Isolating quotes from other works

Another segmentation strategy is to isolate quotes from other works that may be used in your text. Quoting extensively from other literary works is, for example, very common in pre-20th-century novels.

### Segmenation by genre

This segmentation strategy often overlaps with isolating quotes. Segmentation by genre means that you consider if your text belongs to just one literary genre or if different genres are combined. For instance, a novel can contain poetry or newspaper articles (including fictitious ones). A newspaper article can, conversely, contain song lyrics, etc. In the novel [Frankenstein](https://www.gutenberg.org/files/84/84-h/84-h.htm), several poems (by other authors) are quoted:

> Did I request thee, Maker, from my clay
To mould me man? Did I solicit thee
From darkness to promote me?

—Paradise Lost. 

> Like one who, on a lonely road,
Doth walk in fear and dread,
And, having once turned round, walks on,
And turns no more his head;
Because he knows a frightful fiend
Doth close behind him tread.

[Coleridge’s “Ancient Mariner.”] 

> We rest; a dream has power to poison sleep.
    We rise; one wand’ring thought pollutes the day.
We feel, conceive, or reason; laugh or weep,
    Embrace fond woe, or cast our cares away;
It is the same: for, be it joy or sorrow,
    The path of its departure still is free.
Man’s yesterday may ne’er be like his morrow;
    Nought may endure but mutability! 

> ——The sounding cataract
Haunted him like a passion: the tall rock,
The mountain, and the deep and gloomy wood,
Their colours and their forms, were then to him
An appetite; a feeling, and a love,
That had no need of a remoter charm,
By thought supplied, or any interest
Unborrow’d from the eye.

[Wordsworth’s “Tintern Abbey”.]

#### Resources

Hyperscience Resource Center (n.d.). Natural language processing. [https://www.hyperscience.ai/resource/natural-language-processing/](https://www.hyperscience.ai/resource/natural-language-processing/)

Moeng, T., Reay, S., Daniels, A., & Buys, J. (2021). Canonical and Surface Morphological Segmentation for Nguni Languages. In Proceedings of the Second Southern African Conference for AI Research (SACAIR 2021), 6-10 December 2021, Dolphin Coast, KwaZulu-Natal. Communications in Computer and Information Science, Springer. [https://pubs.cs.uct.ac.za/id/eprint/1494/1/Morphological_Segmentation__SACAIR_.pdf](https://pubs.cs.uct.ac.za/id/eprint/1494/1/Morphological_Segmentation__SACAIR_.pdf)

Tal, R., Shmidman, C. S., & Shmidman, A. (2026). Modeling the “dalet” clitic in historical Hebrew texts: A new prefix-segmented BERT model and stylistic analysis. In Proceedings of the 6th International Conference on Natural Language Processing for the Digital Humanities (pp. 121-131). Association for Computational Linguistics. https://aclanthology.org/2026.nlp4dh-1.12.pdf
