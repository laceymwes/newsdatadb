#!/usr/bin/env python
# PSQL python module
import psycopg2

DBNAME = "news"


# connects to db and executes passed query
def get_query_results(query):
    # open DB connection
    db = psycopg2.connect(database=DBNAME)
    # create cursor object from connection object for query execution
    db_c = db.cursor()
    db_c.execute(query)
    ''' fetchall returns queries that have been ran thus far with the current DB
    connection and cursor object
    '''
    results = db_c.fetchall()
    db.close()
    return results


# Question 3
# Print dates where 404 statuses were over 1% total of total status codes
def get_top_404():
    print("The following are dates with over 1% 404 responses:")
    # query statement uses percentage_404_date view created in DB
    query = "select * from percentage_404_date"
    # call get_query_results function and assign dictionary to results variable
    results = get_query_results(query)
    # date = to_char column/field, percentage = percentage_404 column/field
    for date, percentage in results:
        # format and print results
        print(date + " -" + percentage + "% errors")


# Question 1
# print top three most popular articles
def get_pop_articles():
    print("The following are the top three most popular articles:")
    # query statement uses article_popularity view in DB
    query = "select * from article_popularity"
    # call get_query_results function and assign dictionary to results variable
    results = get_query_results(query)
    for title, view_count in results:
        # format and print results
        print("\"" + str(title) + "\" - " + str(view_count) + " views")
    print("\n")


# Question 2
# print authors in order of popularity
def get_pop_authors():
    print("The following are the authors, ordered by article popularity:")
    # query statement uses author_popularity view in DB
    query = "select * from author_popularity"
    # call get_query_results function and assign dictionary to results variable
    results = get_query_results(query)
    for author, views in results:
        # format and print results
        print(str(author) + " - " + str(views) + " views")
    print("\n")


get_pop_articles()
get_pop_authors()
get_top_404()
