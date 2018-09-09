#!/usr/bin/env python3
import psycopg2

DBNAME = "news"
FILENAME = "result.txt"

sql_get_top_three_artciles = "select articles.title, count(*) as views from log \
left join articles on log.path = concat('/article/', articles.slug) \
where log.path <> '/' \
group by articles.title \
order by views desc limit 3"

sql_get_top_authors = "select authors.name, count(*) as views from log \
left join articles on log.path = concat('/article/', articles.slug) \
left join authors on articles.author = authors.id \
where log.path <> '/' and authors.id is not null \
group by authors.id \
order by views desc"

sql_get_error_days = "select t.date, round(100.0 * sum(status)/count(*), 2) \
from (select to_char(time, 'MON dd,yyyy') as date, \
case status when '200 OK' then 0 else 1 end as status from log) as t \
group by t.date \
having ((100.0 * sum(status)/count(*)) > 1)"


def execute(sql):
    """Return sql result"""
    db = psycopg2.connect(database=DBNAME, user='vagrant')
    c = db.cursor()
    c.execute(sql)
    result = c.fetchall()
    db.close()
    return result


def write_file(file_name, res):
    print (res)
    file_object = open(file_name, 'a')
    file_object.write(res + '\n')
    file_object.close()


def main():
    # 1. What are the most popular three articles of all time?
    top_articles = execute(sql_get_top_three_artciles)
    res = "1. What are the most popular three articles of all time?"
    write_file(FILENAME, res)
    for article in top_articles:
        res = '\"' + str(article[0]) + '\" -- ' + str(article[1]) + ' views'
        write_file(FILENAME, res)

    # 2. Who are the most popular article authors of all time?
    top_authors = execute(sql_get_top_authors)
    res = "\n2. Who are the most popular article authors of all time?"
    write_file(FILENAME, res)
    for author in top_authors:
        res = author[0] + ' -- ' + str(author[1]) + ' views'
        write_file(FILENAME, res)

    # 3. On which days did more than 1% of requests lead to errors?
    err_days = execute(sql_get_error_days)
    res = "\n3. On which days did more than 1% of requests lead to errors?"
    write_file(FILENAME, res)
    for err in err_days:
        res = err[0] + " -- " + str(err[1]) + "% errors"
        write_file(FILENAME, res)

if __name__ == "__main__":
    main()
