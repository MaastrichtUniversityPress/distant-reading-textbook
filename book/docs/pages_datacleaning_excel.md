# Data cleaning in Excel

## Search and replace

Excel's *Find and Replace* option (Ctrl+H) is the first tool to reach for when standardising inconsistent entries, such as correcting misspelled names or unifying "UK" and "United Kingdom". It is advisable to work on a copy of your data before performing a bulk replacement, as unintended changes can be difficult to trace afterwards. Note that replacing a value which appears in many different contexts risks introducing errors, so always review the number of matches Excel reports before confirming the change.

## Conditional highlighting

Conditional formatting (Home > Conditional Formatting) allows you to highlight cells automatically based on rules, for example flagging duplicate entries or locating blank cells. This is particularly useful for spotting inconsistent data entry, such as dates in mixed formats or names spelled in more than one way. Because highlighting is visual rather than destructive, it is a safe method for auditing a dataset before you begin cleaning it.

## Sorting and custom filters

Sorting your data (Data > Sort) brings identical or similar values together, which makes inconsistencies such as "Amsterdam" and "amsterdam " immediately visible when scrolling through the column. Excel's sort dialogues also allow multi-level sorts, for example ordering by country first and then by city within each country. Custom filters (Data > Filter) go one step further by displaying only rows that meet specific criteria, such as all entries from a particular year or all cells containing a given keyword. Filtering is non-destructive: rows that do not match are hidden rather than deleted, so you can examine subsets of your data without losing anything. Always ensure your data has a single header row before sorting or filtering, otherwise Excel may treat part of your data as labels.

## Functions

Perhaps the most advanced way to use Excel for data cleaning is to work with so-called functions. These are essentially code snippets that you can insert in selected cells after typing "=" and opening brackets to perform standardised actions on other selected cells. 
Below are the most common functions that you will want to use for data preparation in the humanities and social sciences.

### Lookup

Lookup functions retrieve a value from one part of your spreadsheet and insert it into another, which makes them ideal for combining data from different tables. The most widely used variant is VLOOKUP, which searches for a key (such as an ID number) in the first column of a table and returns a value from another column in the same row. This is essential when, for example, you wish to attach place names or occupations to a list of persons recorded in a separate sheet.

```
=VLOOKUP(A2, Sheet2!A:D, 3, FALSE)
```

### String splitting

Humanities data frequently stores several pieces of information in one cell, such as "Barget, Monika" or "Amsterdam, Netherlands". String splitting functions separate such combined values into individual columns, which is a prerequisite for sorting or analysing each component separately. Excel's Text to Columns wizard (Data > Text to Columns) offers a menu-driven alternative, but the TEXTSPLIT function (or the older combination of LEFT, MID and FIND) gives you more control.

```
=TEXTSPLIT(A2, ",")
```

### Date conversions

Time value imported from humanities databases or the web are often stored in varying format and need conversion to be machine-readable.
A common case in historical research is converting British-style dates (day/month/year, e.g. 2/8/1567) into the ISO standard YYYY-MM-DD (e.g. 1567-08-02).
Another use case would be to write dates using the names of months as text as digits only.

Example (presumably shown in Excel cell A1) | Formula |
 |---|---|
 | `2/8/1567` | `=TEXT(DATE(RIGHT(A1,4), MID(A1, FIND("/",A1)+1, FIND("/",A1,FIND("/",A1)+1)-FIND("/",A1)-1), LEFT(A1, FIND("/",A1)-1)), "yyyy-mm-dd")` |
 | `02/08/1876` | `=TEXT(A1, "yyyy-mm-dd")` |
 | `5 May 2026` | `=TEXT(DATEVALUE(A1), "yyyy-mm-dd")` |
