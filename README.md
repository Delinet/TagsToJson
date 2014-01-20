TagsToJson
==========

A Python module to retrieve all the links and the text about specified tag


The module use the Beautiful Soup pythom library.
To use TagsToJson module You must install BeautifulSoup or import the bs4 folder in Your main root python application folder.

You can retrieve the last release of BeautifulSoup @:
Main page:http://www.crummy.com/software/BeautifulSoup/
Download:http://www.crummy.com/software/BeautifulSoup/bs4/download/
Documentation:http://www.crummy.com/software/BeautifulSoup/bs4/doc/


How to use the python module
============================

It's a simple function to retrieve a json file with this structure:

You must pass - as a couple of string parameter(s) - the url to parse and the tag to retrieve
example: tagtojson('www.github.com','div')

The function return a json string structured as:

{ 
  url: [a single value about the url of the html document]
  title: [a single value about the title of the html document]
  links: [a list of the all links tagged in the html document]
  tags: [a list of obj about tags in the html document - tag obj is structured: tag_html alias the tag in html way,   tag_text alias the text of the tag]
}
