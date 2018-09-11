# Project Logs analysis
This project is creating a reporting tool to prints out statistical base on the data in the news database. 
By analyzing the logs of users browsing web pages, We can see the popularity of these articles and the authors. 
By analyzing the state of requests in logs, we can statistic of error rate.

## Usage
* Environmental requirements
    * we have two methods to deploy the environment.  
    * Method One: Full deployment environment by ourself
         - Install postgresql, pgAdmin and python3, we can download installation package from official website. 
         - According to the *Environmental configuration*, create database, user, role, and import the data.
    * Method Two: with the help of vagrant
         - Install virtual machine, VirtualBox
         - Install Vagrant
         - Download the VM configuration, FSND-Virtual-Machine.zip, then create vagrant dir, put it in, and run the command vagrant up.
            > When vagrant up is finished running, you will get your shell prompt back. 
            > At this point, you can run vagrant ssh to log in to your newly installed Linux VM!
         - Running the database
         - Download data, and put this file into the vagrant directory
         - cd into the vagrant directory and use the command psql -d news -f newsdata.sql. it can import the data to news database.

* Environmental configuration
    1. Create database news
    2. Create user: create user vagrant with password 'xxxxxx'
    3. Create role: create role vagrant LOGIN
    4. Import the data into the database, execute newsdata.sql: 
        - psql -d news -f C:\full-stack\4.Project-Logs-Analysis\newsdata.sql -U vagrant 
        - Execute newsdata.sql could create three tables: articles, authors, log. And insert the data. 
        - The authors table includes information about the authors of articles.
        - The articles table includes the articles themselves.
        - The log table includes one entry for each time a user has accessed the site, and read the articles.

* Code description
    * log_analysis.py has an execute function. It is used to connect to database and execute sql. Then we solved three questions through call this function.
        * What are the most popular three articles of all time? 
        * Who are the most popular article authors of all time? 
        * On which days did more than 1% of requests lead to errors?
    * we should use idle to run this log_analysis.py in window, or execute python ./log_analysis.py in linux,  then it will generate a result.txt which printed out the three question result.
