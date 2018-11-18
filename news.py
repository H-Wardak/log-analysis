#!/usr/bin/env python3
import psycopg2


# connect to, and fetch result from DB
# It takes two arguments, DB name and the query
def get_query_rslt(db_name, query):
    try:
        db = psycopg2.connect('dbname={}'.format(db_name))
    except psycopg2.Error as e:
        print "Unable to connect!"
        print e.pgerror
        print e.diag.message_detail
        sys.exit(1)
    else:
        print("Connected to DB")
        cursor = db.cursor()
        cursor.execute(query)
        output = cursor.fetchall()
        db.close()
        return output


def get_top3_articles():
    query = "SELECT title, count FROM articles, \
    (SELECT slug, count(path) AS count FROM articles, log \
    WHERE log.path = '/article/' || articles.slug GROUP BY slug) AS subq WHERE\
    articles.slug = subq.slug ORDER BY count DESC LIMIT 3;"
    output = get_query_rslt('news', query)
    f.write("1- What are the most popular three articles of all time?\n")
    for article, views in output:
        f.write("{} --\t {} views\n".format(article, views))


def get_top_authors():
    query = "SELECT name, count(*) AS views FROM authors, log, articles \
    WHERE authors.id = articles.author AND log.path = '/article/' || slug AND \
    status ='200 OK' GROUP BY name ORDER BY views DESC;"
    output = get_query_rslt('news', query)
    f.write("\n2- Who are the most popular article authors of all time?\n")
    for author, views in output:
        f.write("{} --\t {} views\n".format(author, views))


def get_most_error_day():
    query = "CREATE VIEW all_req AS SELECT to_char(time,'YYYY-MM-DD') \
    AS date, count(*) AS sum FROM log GROUP BY date;\
    CREATE VIEW err_req AS SELECT to_char(time,'YYYY-MM-DD') \
    AS date, count(status) AS error FROM log WHERE status !='200 OK' \
    GROUP BY date; \
    SELECT cast((cast(error AS float)/cast(sum AS float))*100 \
    AS float) AS error_per, all_req.date FROM all_req, err_req \
    WHERE all_req.date = err_req.date ORDER BY error DESC;"
    output = get_query_rslt('news', query)
    f.write("\n3. On which days did more than 1/% of requests \
    lead to errors?\n")
    for error, date in output:
        if(error > 1.0):
            f.write("{} -- {:.2f} % errors".format(date, error))


f = open('news_log_output.txt', 'w')
get_top3_articles()
get_top_authors()
get_most_error_day()
print('DONE')
