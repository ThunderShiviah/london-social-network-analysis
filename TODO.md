2015-03-11:
- Currently the scraper outputs name and location.
- The location looks good but the names have a lot of unwanted marks and lines.
- Furthermore, the names have commas, numbers, and \n symbols in them.
- Finally, the names are not nested under location which is critical. 
- The names could be split on commas to get the number of copies (if no copy ammount is listed we can assume 1 copy). This could be accomplished by using regular expressions.

The most important thing for next time is to figure out how to nest names under location.
