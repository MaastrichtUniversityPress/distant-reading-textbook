# Sample analysis "Miley Cyrus’s VMA 2013 Performance"

:book: I generally use this case study in my data feminism lecture to showcase possible feminist and intersectional readings.

## The root of the VMA 2013 controversy

Miley Cyrus’s 2013 MTV Video Music Awards (VMA) performance with Robin Thicke remains one of the most debated moments in pop culture history. They jointly performed Thicke’s song *"Blurred Lines"* with its controversial lyrics *"I know you want it"*, which had previously been criticized for glorifying rape culture in pop music. For Cyrus, who rose to fame as a Disney Channel star in *Hannah Montana* (2006–2011), the performance marked a deliberate break from her teen idol image (Kennedy, 2014). Yet, this transition also resulted in criticism by fans and fellow celebrities (Overell, 2013). Cyrus's performance was characterized by sexually suggestive choreography, including twerking, a dance style rooted in Black culture, and interactions with Black female backup dancers. This challenged traditional notions of female stardom and family-friendly entertainment, but also raised questions about racial representation on stage. 

As a white European woman with limited exposure to U.S. pop culture, my own awareness of the "scandal" came when academic circles began debating the show and its wider implications. This discussion was primarily driven by established news outlets and targeted audiences interested in cultural controversies. (Fleetwood, 2011) But what about the immediate reactions on social media? On Twitter, the then-leading platform, the event broke all coverage records and incited 306,000 tweets per minute while the show was on-going. Selecting a dataset of 100,000 early tweets as a sample dataset, I will identify how the key themes of family values, gender, and race were discussed on Twitter and in how far this confirms and contradicts opinions circulated by print media and television channels in the days following the VMA 2013. Ideally, these findings can also give us insights into pop culture fandom at the time more generally.

## Print media and TV reactions

During and after VMA2013, one of the most frequently shared posts on social media was a photo of actor Will Smith family’s alleged reaction, which, although taken out of context, expressed how many people felt about the performance: The actor, his wife and two sons are shown gaping in awe, with facial expressions oscillating between admiration and shock. This dichotomy was also reflected in news articles and TV talk shows that covered Miley Cyrus's performance. While Miley’s most loyal fans appreciated her performance as "sexy," especially families watching the show felt it was extreme and tasteless. Some parents were worried about the impact on teenage girls. Other criticism focused on the artistic side of the show. Speaking to USA Today, Cher called the performance “so bad”: “[Miley] could have come out naked, and if she'd just rocked the house, I would have said, 'You go, girl.' It just wasn't done well. She can't dance, her body looked like hell, the song wasn't great, one cheek was hanging out." More general cultural aspects of the performance were discussed by cultural journalists such as Hadley Freeman (The Guardian): "Miley Cyrus's twerking routine was cultural appropriation at its worst. Cyrus's act was less a homage to hip-hop and more a minstrel show. For cultural cross-pollination, give me the Notting Hill carnival any day."

## Dataset overview and structural insights

This analysis uses a selection of 100,000 English-language tweets published at the time of the VMA performance. This dataset was collected using the official academic API provided by Twitter before Elon Musk acquired the platform. The data collection query used to gather these tweets included a combination of keywords to ensure relevance to my research question and exclude spam posts and mere retweets:

("miley" OR "cyrus" OR #miley OR #mileycyrus OR #robinthicke OR "robin" OR @mileycyrus) ("vma2013" OR #vma2013 OR "performance" OR "vma" OR #vma OR #twerking OR "tv" OR "stage" OR "women" OR "children" OR "family" OR "culture" OR "black" OR "appropriation" OR "hip hop" OR "people of color" OR "dancers" OR "finger") lang:en -is:retweet

## Limitations

The collected data set is naturally dominated by the names of the two performers, which is why *"Miley," "Cyrus," "Robin,"* and *"Thicke"* are the most frequent terms. Many tweets are brief, emotional reactions rather than elaborate critiques, and several contain more than one hashtag. The following example consists of just one sentences which asks if Miley was on drugs: *"Miley Cyrus Was She On Molly During the VMA Show? #molly #MileyCyrus #VMAs."* Some tweets use trending hashtags to promote unrelated content, such as *#Beats* headphones or other artists like *#Gaga* and *#Bieber*. Twitter users heavily relied on sharing links to video clips relating to the event, which means that many URLs are present in the data set. Emojis, images, and video links, which are critical to understanding the full scope of reactions, however, are not captured in the text-only dataset.

## Theory

Data feminism and intersectionality provide critical frameworks for analyzing Miley Cyrus’s VMA 2013 performance because the event exposes systemic power imbalances in gender, race, and media representation. The sexualization of Cyrus, a former Disney star, underscores the double standards women face in entertainment, aligning with data feminism’s emphasis on challenging structural inequalities. The public backlash further reveals how discussions of femininity and race are shaped by institutional power, including media producers, audience expectations, and societal norms. Finally, an intersectional lens helps dissect the layered identities (gender, race, class) involved in both the performance and its reception, making it a compelling case for critical inquiry.

## Voyant Tools

Voyant Tools is well-suited for analyzing larger datasets because it visualizes patterns and trends.Social media data often contains repetitive phrases and recurring hashtags, which Voyant’s word frequency visualizations can quickly summarize. The trends tool is especially useful for tracking how discussions evolve over time, even in highly repetitive datasets. Additionally, the context tool allows researchers to examine how specific keywords (e.g., "black," "women") are used in actual tweets. Finally, Voyant’s co-occurrence tools (e.g., Terms Berry, Links) help uncover relationships between frequently repeated terms.

## Main agents and their roles

The primary agents in the dataset are Miley Cyrus, Robin Thicke, the Black female dancers, media figures and outlets, and the Smith family, whose alleged reaction photo went viral.
The gender and ethnicity of these agents matter. 
[...]

## Analyzing emotions

The dataset reveals a polarized emotional landscape. Positive emotions include terms like *"love," "good,"* and *"sexy"* appearing frequently. These terms are used by Cyrus’s fans who appreciated her new image. Negative emotions are dominated by words like *"disgusting," "tasteless,"* and *"embarrassing"*, which particularly came from viewers who found the performance inappropriate for family audiences or a bad model for young girls. Mockery and insults are also present in many tweets using derogatory language, such as *"Miley looked like hell"* or *"worst performance ever."*

When placed in the context tool, these emotions often reveal personal attacks, gendered and racialized language, and a focus on entertainment value over serious critique.

## Keywords in context

The term *"women"* often appears in discussions about sexualization, double standards, and feminist critiques. The term *"black"* is used in diverse and often problematic ways, ranging from discussions about cultural appropriation to racial stereotypes and ambiguity. The term *"appropriation"* appears in only 439 tweets in the entire dataset, indicating that the academic debate was not a central theme for most Twitter users.

## Narrative developments in trends

Using the trends tool in Voyant, we can track how discussions evolved over time. The terms *"black" and "white"* spike early in the tweets, reflecting immediate reactions to the racial dynamics of the performance. The terms *"dancers" and "twerk*"* remain consistent, highlighting the centrality of the dance in the conversation. The term *"rape"* appears less frequently but is tied to critiques of *"Blurred Lines"* and its lyrics. The terms *"women" and "children"* often co-occur with moral critique.

## Discussion

A data feminist analysis of this dataset reveals several key insights. Opinion on the performance is divided, with negative comments tending to be insulting or mocking rather than constructive. Criticism of a sexualised image of women and "rape culture" is not a central theme of the Twitter debate. Similarly, cultural appropriation is only discussed by a minority of users in the data, whereas many comments display shocking combinations of misogyny and racism. There is no agreement on what "femininity" and/or "blackness" are, as "black" is used to describe various attitudes and behaviours on stage. The entertainment value of the event dominates the reactions, and a serious reflection on culture is only present in a minority of comments. Changes in the representation of women on stage cannot be discussed without analysing the (powerful) positions of TV producers, managers, choreographers, bloggers etc., who are also tagged in this Twitter dataset as acted as core opinion makers...

## Conclusion

This dataset highlights the complex interplay of gender, race, and power in public reactions to pop culture. While feminist and intersectional critiques are present, they are often drowned out by entertainment-focused or derogatory discourse. This underscores the need for further research into how social media shapes and limits public debates on cultural appropriation, sexuality, and representation. After all, Miley Cyrus's case is not unique as other stars undergoing a sudden and public revision of their image have experienced similar backlash (Britney Spears and Justin Bieber). A comparative analysis of social media reactions to controversial star performances from different contexts would be interesting.

### Cited works

- Blue, M. G. (2013). The best of both worlds? Youth, gender, and a post-feminist sensibility in Disney's *Hannah Montana. Feminist Media Studies, 13*(4), 660–675. https://doi.org/10.1080/14680777.2012.724024
- Fleetwood, N. R. (2011). *Troubling vision : performance, visuality, and blackness.* University of Chicago Press. http://chicago.universitypressscholarship.com/view/10.7208/chicago/9780226253053.001.0001/upso-9780226253022
- Kennedy, M. (2014). Hannah Montana and Miley Cyrus: ‘becoming’ a woman, ‘becoming’ a star. *Celebrity Studies, 5*(3), 225–241. https://doi.org/10.1080/19392397.2013.839349
- McRobbie, A. (2004). Post‐feminism and popular culture. *Feminist Media Studies, 4*(3), 255–264. https://doi.org/10.1080/1468077042000309937
- Overell, R. (2013, August 27). Change in packaging presents a fresh Miley Cyrus commodity. *The Conversation.* https://theconversation.com/change-in-packaging-presents-a-fresh-miley-cyrus-commodity-17523
- Weidhase, N. (2015). ‘Beyoncé feminism’ and the contestation of the Black feminist body. *Celebrity Studies, 6*(1), 128–131. https://doi.org/10.1080/19392397.2015.1005389