import psycopg2

DBNAME = "news"

sql_get_top_three_artciles = "select articles.title, t.views from articles \
right join (select log.path, count(*) as views from log \
where status = '200 OK' and path <> '/' \
group by path order by views desc limit 3) as t \
on ('/article/' || replace(articles.slug, ' ', '-')) = t.path"

sql_get_top_authors = "select authors.name, sum(t.views) from articles \
right join (select log.path, count(*) as views from log \
where status = '200 OK' and path <> '/' group by path \
order by views desc ) as t \
on ('/article/' || replace(articles.slug, ' ', '-')) = t.path \
left join authors on articles.author = authors.id \
group by authors.name"

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

# 1. What are the most popular three articles of all time?
top_articles = execute(sql_get_top_three_artciles)
print ("1. What are the most popular three articles of all time?")
for article in top_articles:
    print ('\"' + str(article[0]) + '\" -- ' + str(article[1]) + ' views')
print ("----------------------\n")

# 2. Who are the most popular article authors of all time?
top_authors = execute(sql_get_top_authors)
print ("2. Who are the most popular article authors of all time?")
for author in top_authors:
    print (author[0] + ' -- ' + str(author[1]) + ' views')
print ("----------------------\n")

# 3. On which days did more than 1% of requests lead to errors?
err_days = execute(sql_get_error_days)
print ("3. On which days did more than 1% of requests lead to errors?")
for err in err_days:
    print (err[0] + " -- " + str(err[1]) + "% errors")