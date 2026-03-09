# A brief introduction to distant reading

## What do (digital) humanities scholars define as text?

## What is distant reading?

Distant reading is - unsurprisingly - the opposite of close reading. While close reading means
that a human reader deeply engages with a text, processing it line by line and word by word,
distant reading is a computational method that goes from analysing individual texts to
examining large corpora of documents simultaneously. Rather than focusing on detailed interpretation of single works, distant reading treats texts as data that can be explored through statistical analysis.

Researchers might measure word frequencies, detect thematic clusters, identify linguistic patterns, or visualise narrative developments. Importantly, distant reading does not eliminate the need for careful human interpretation. Instead, it creates a dialogue between computational analysis and humanistic inquiry. This is why most humanities and social sciences scholars do not apply distant reading as a stand-alone method, but use it in combination with close reading or other qualitative research methods, such as interviewing and focus groups. This approach is often referred to as "middle distance reading". (Hearst etc.)

## Steps in distant reading

Conducting a distant reading analysis typically involves several stages. The first step is data collection / corpus building, which may involve retrieving texts from online platforms, digital archives, or curated datasets. Depending on the research question, this might include social media posts, news articles, literary texts, or other forms of digital content.

Once data has been collected, the next stage is data preparation or cleaning. Textual data found on the web often contains inconsistencies such as formatting errors, duplicated content, or material irrelevant to a text-centred analysis (e.g. emojis, images, videos, or animations). Preparing the data may involve separating metadata from the corpus, normalising spelling, or converting file formats like MS Word into plain text (TXT) suitable for computational analysis.

The third stage is the analysis itself. Researchers apply techniques from natural language processing (NLP), such as topic modelling, sentiment analysis, or frequency analysis. Visualisation tools can also be used to explore patterns in the data and communicate findings.

Finally, the results must be interpreted within their broader cultural, historical, or social context. Computational methods reveal statistical patterns, but these patterns require careful interpretation. Researchers must consider the limitations and biases of their datasets as well as the assumptions embedded in the algorithms used.

## Analysing web content through distant reading

The rapid expansion of digital communication has results in large amounts of textual data available for analysis. Social media platforms, online news sites, discussion forums, and digital archives can all be studied using distant reading methods, provided that they permit (automated) data collection for research purposes.

As mentioned before, analysing web content often requires specific techniques for collecting and preparing data. Researchers may use web scraping tools or platform APIs to retrieve posts, comments, or articles. It is important to note that not all platforms allow research use and / or facilitate easy access. Because web-based data is very heterogeneous, additional steps are also necessary to clean and structure the data before analysis.

So-called application programming interfaces (APIs) allow you to collect online data in table formats (CSV) with different columns for the actual content (posts and replies) as well as metadata (time stamps, user names, location data, etc.). For text analysis, the posts and replies are the core information needed. Depending on the tools used for analysis, this information may have to be written to TXT files first. 

## Challenges of working with web content

Web data also presents unique methodological and ethical challenges. Researchers must approach the analysis of online content with care and pay attention to ethical guidelines and responsible data practices. Where possible, researchers should use an official application programming interface (API) provided by the service from which they want to extract data. APIs can either be accessed via user interfaces or via code (e.g. using scripts in Python or R).

Unfortunately, Twitter/X has become increasingly restrictive toward API access and generally defines stricter usage rules. Reddit, TikTok and Instagram raise similar concerns. Here, data analysts often operate with 3rd-party apps or HTML-scraping, but students should consult with their supervisors before using any such methods. Where platform restrictions to data use apply, you should also consult the Internet Research Ethics Guidelines 3.0 (IRE 3.0), developed by the Association of Internet Researchers (AoIR). This guide offers practical guidance for conducting ethical research in online environments, based on three ethical norms: respect for persons, beneficence, and justice. It also stresses ethical pluralism and cross-cultural awareness. Ethical decisions are not universally fixed but vary depending on context and the research scenario. Therefore, IRE 3.0 focuses on asking the right questions rather than giving rigid answers. If downloading text, images or video content from social media is methodologically justified and ethically defensible even when no official API access exists, students may download data as long as they can ensure GDPR-compliant data storage and data processing. This means, for example, that they will only use offline tools like NoScribe or aTrain for the automated transcription of audio and video. In addition, researchers must anonymise sensitive material.

Key areas of concern in working with online data defined by IRE 3.0 are the following:

- Informed consent: Especially challenging in big data contexts, where obtaining consent from thousands of users may be unfeasible. In such cases, researchers should minimise risks, use pseudonymisation, and carefully consider the timing and scope of consent (e.g., at the dissemination stage for quotes).

- Ethical reflection: IRE 3.0 outlines different stages of a research project (design, data collection, analysis, dissemination) at which researchers should reflect ethically.

- Researcher (and user) safety: The guidelines highlight the importance of protecting researchers (and other internet users) from online harassment, emotional harm, or legal consequences, especially in politically sensitive or extremist content research.

- Privacy and context: Researchers must consider whether online data is genuinely public and whether users expect privacy — even in seemingly open forums. Contextual integrity and the user’s understanding of public/private distinctions are essential.

- Cultural and legal diversity: Ethical standards differ globally. Researchers must respect local norms and understand legal frameworks like GDPR in Europe or differing expectations of individual consent across cultures.

- Power and platform dynamics: Social media platforms’ policies (e.g. terms of service) can affect what data researchers can access. These platforms also shape user behavior, which should be critically discussed.

Students are encouraged to begin by identifying the ethical issues which their research raises and bring up all concerns with their supervisors as early as possible.

## Recommended readings

Amsrud, M. B. (2023). Internet Research Ethics – Resources and Challenges. A qualitative study. (MA thesis) https://brage.inn.no/inn-xmlui/handle/11250/3108829

Buchanan, E. A. (2011). “Internet Research Ethics: Past, Present, Future”. In Ess and Consalvo (eds.), The Handbook of Internet Studies, pp. 83–108. Oxford: Blackwell Publishing Ltd.

Elgesem, D. (2015). “Consent and information - ethical consideration when conducting research on social media”. In Fossheim and Ingierd (eds.), pp. 14–34.

franzke, aline shakti, Bechmann, Anja, Zimmer, Michael, Ess, Charles and the Association of Internet Researchers (2020). Internet Research: Ethical Guidelines 3.0. https://aoir.org/reports/ethics3.pdf

Locatelli, E., franzke, a. s., Ess, C. M. (2023). Introduction. Over Twenty Years of Internet Research Ethics: Key Concepts and Future Challenges, COMUNICAZIONI SOCIALI, 2023 (2), pp. 131-138. https://hdl.handle.net/10807/270782

