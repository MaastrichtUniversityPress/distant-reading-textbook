# Open Refine for cleaning spreadsheet data

Open Refine is a powerful tool for the manipulation of data in table format. You can use Open Refine directly in the UM DSRI or install it on your local machines.  
In our course, Open Refine helps us filter podcast reviews to create sub-collections of data for analysis in Voyant Tools.

## Using filters in Open Refine

You can filter the data displayed in OpenRefine by applying a ‘Text Filter’, which looks for a particular piece of text appearing in a column. Text filters are applied by clicking the drop-down menu at the top of the column you want to apply the filter to and choosing **Text filter**. The filter options appear in the left-hand panel (see Figure 1). Simply type in the text you want to use in the Filter to display only rows which contain that text in the relevant column. You can also use [regular expressions](https://librarycarpentry.github.io/lc-data-intro/04-regular-expressions) in the filter (Library Carpentry, n.d.). 

It is very important to note that when you have filtered the data displayed in OpenRefine, any operations you carry out will apply only to the rows that match the filter – that is, the data currently being displayed. This also means that only the current selection will be saved when you export your data while a filter is active!

[![Figure 1](../screenshots_distant_reading/OpenRefine_filter.png)](../screenshots_distant_reading/OpenRefine_filter.png)

**Figure 1:** Applying a text filter to the *review* column to find all reviews mentioning “victims”.

## Working with facets in Open Refine

Facets are one of the most useful features of OpenRefine and can help both get an overview of the data in a project as well as helping you bring more consistency to the data. A ‘Facet’ groups all the values that appear in a column, and then allows you to filter the data by these values and edit values across many records at the same time. The simplest type of Facet is called a ‘Text facet’. This simply groups all the text values in a column and lists each value with the number of records it appears in. The facet information always appears in the left-hand panel in the OpenRefine interface (see Figure 2).

To create a Text Facet for a column, click on the drop-down menu at the top of the publisher column and choose `Facet -> Text Facet`. The facet will then appear in the left-hand panel. The facet consists of a list of values used in the data. You can filter the data displayed by clicking on one of these headings. You can include multiple values from the facet in a filter at one time by using the `Include` option, which appears when you put your mouse over a value in the Facet. You can also `invert` the filter to show all records which do not match your selected values. This option appears at the top of the Facet panel when you select a value from the facet to apply as a filter.

Facets can be a great way to select podcast reviews by user names, time periods, or star ratings.

[![Figure 2](../screenshots_distant_reading/OpenRefine_textfacet.png)](https://github.com/MonikaBarget/distant-reading/tree/main/screenshots_distant_reading/OpenRefine_textfacet.png)

**Figure 2**: Facet applied to the *user* column, showing all usernames and the number of reviews written.

The steps involved in exporting and saving your data are illustrated in Figures 3 and 4 below. However, please also read the documentation for "Exporting your Work" in the official [Open Refine (n.d.)](https://openrefine.org/docs/manual/exporting) documentation!


[![Figure 3](../screenshots_distant_reading/OpenRefine_export.png)](https://github.com/MonikaBarget/distant-reading/tree/main/screenshots_distant_reading/OpenRefine_export.png)

**Figure 3**: Using the *Export* option to save a selected subset of the data to a new file.


[![Figure 4](../screenshots_distant_reading/OpenRefine_saverawtext.png)](https://github.com/MonikaBarget/distant-reading/tree/main/screenshots_distant_reading/OpenRefine_saverawtext.png)

**Figure 4**: Raw text from the *review* column copied into a .txt file.

The following YouTube video by Monika explains the process of filtering data in Open Refine and exporting them step-by-step:

[![Thumbnail](https://img.youtube.com/vi/oMWIUf5_9jM/maxresdefault.jpg)](https://youtu.be/oMWIUf5_9jM?si=ibxc2zxcn335uGOo)

The focus is on using a general text filter to find keywords and using the facet filter to explore rankings (DigitalHistory, 2023). However, OpenRefine has many other
exciting functionalities not covered in this brief introduction! If you want to learn more, check out other videos shared by researchers and librarians on YouTube. One [Open Refine tutorial provided by researchers from Edinburgh](https://www.youtube.com/watch?v=wfS1qTKFQoI) does not only explain editing spreadsheets but also covers uploading data easily to Wikidata, which may be of interest to you in the future (Wikimedian in Residence – University of Edinburgh, 2019).

## Cited works and further readings

- Batrinca, B., & Treleaven, P. C. (2015). Social media analytics: A survey of techniques, tools and platforms. *AI & Society, 30*(1), 89–116. https://doi.org/10.1007/s00146-014-0549-4
- DigitalHistory. (2023, December 15). *Sorting and exporting data in Open Refine* [Video]. YouTube. https://youtu.be/oMWIUf5_9jM
- Ham, K. (2013). OpenRefine (version 2.5). *Journal of the Medical Library Association, 101*(3), 233–234. https://doi.org/10.3163/1536-5050.101.3.020
- Library Carpentry. (n.d.). *Regular expressions*. https://librarycarpentry.github.io/lc-data-intro/01-regular-expressions.html
- Miller, M., & Vielfaure, N. (2022). OpenRefine: An approachable open tool to clean research data. *Bulletin – Association of Canadian Map Libraries and Archives*, (170). https://doi.org/10.15353/acmla.n170.4873
- OpenRefine. (n.d.). *Exporting data.* https://openrefine.org/docs/manual/exporting
- Schöch, C. (2013). Big? Smart? Clean? Messy? Data in the humanities. *Journal of Digital Humanities, 2*(3).https://journalofdigitalhumanities.org/2-3/big-smart-clean-messy-data-in-the-humanities-by-christof-schoech/
- Wikimedian in Residence – University of Edinburgh. (2019, August 21). *OpenRefine beginners tutorial* [Video]. YouTube. https://youtu.be/wfS1qTKFQoI




