# Log Analysis Project
This project is creating a reporting tool to prints out statistical base on the data in the database. We use psycopg2 module in python to connect to the postgre database.

## Usage
* Environmental requirements
    * postgresql
    * python3

* Environmental configuration
    1. Create database news
    2. Create user: create user vagrant with password 'xxxxxx'
    3. Create role: create role vagrant LOGIN
    4. Import the data into the database, execute newsdata.sql: 
        - psql -d news -f C:\full-stack\4.Project-Logs-Analysis\newsdata.sql -U vagrant 
        - Execute newsdata.sql could create three tables: articles, authors, log. And insert the data. 

* Code description
    * log_analysis.py has an execute function. It is used to connect to database and execute sql. Then we solved three questions through call this function.
        * What are the most popular three articles of all time? 
        * Who are the most popular article authors of all time? 
        * On which days did more than 1% of requests lead to errors?
    * result.txt is printed out.
