# Identifying and analysing spatial information in texts

## Why visualising spatial information can be relevant

When working with texts that contain spatial information, such as people's birth places or travel destinations, you might want to visualize this information on a map to better understand distances between the entities mentions or trace entire travel routes. This can, indeed, be a great add-on to other visualisation techniques in text analysis, but it is often difficult to accomplish. Tools like **Voyant** offer features for creating maps from text, such as [DreamScape](http://www.voyant-tools.org/docs/tutorial-dreamscape.html). However, this tool only works well in a minority of use cases.

### Challenges with Voyant’s DreamScape

1. **Lack of contextual analysis**: DreamScape does not analyze the context in which place names appear. This can lead to inaccuracies, such as plotting **personal names as places** if they resemble geographic terms.
2. **Anglophone bias**: DreamScape tends to work best with English-language texts and is more effective at identifying places in the **UK and US**. Non-English place names or locations outside these regions may not be recognized accurately or at all.
3. **Ambiguity in place names**: Many place names are shared across different regions or countries. Without contextual clues, DreamScape may misidentify or misplace these locations on the map.

### Better alternatives for mapping

For more accurate and reliable map-making, beginner tools like [Palladio](https://hdlab.stanford.edu/palladio/) are often a better choice. Unlike Voyant, Palladio requires you to **create your own spreadsheet** of verified place names and their coordinates first. This is, of course, more time-consuming but ensures that you have full control over the data and that only accurate information will be shown. If you’re working with texts that contain diverse or non-standard place names, investing time in preparing a verified dataset for tools like Palladio will yield far more reliable and insightful visualizations.
