# Log Analysis

This project is using News Database containing number of articles and statistics about the viewers. The aim of project is to extract some information about the most influences of the articles and authors. Also, checking if there were any network issues in the website. It answering the follwoing questions:
1- What are the most popular three articles of all time?
2- Who are the most popular article authors of all time?
3- On which days did more than 1% of requests lead to errors?


## How to Run?
The database in this project is running PostgreSQL. 
- Download the data [here], unzip it
- the file is called **newsdata.sql** and the database name is **news**
- load the data into a directory: ```psql -d news -f newsdata.sql ```
- Run news.py script
- The result is written in **news_log_output.txt**

## Implementation
The script contains three main functions to asnwer each of the above question and write output to a file, plus separate function for connecting and fetching data from database.




[here]: <https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip>
