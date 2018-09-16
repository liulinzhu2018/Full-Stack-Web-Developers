# Project Logs analysis
This project is creating a reporting tool to prints out statistical base on the data in the news database. 
By analyzing the logs of users browsing web pages, We can see the popularity of these articles and the authors. 
By analyzing the state of requests in logs, we can statistic of error rate.

## Usage
* Environmental requirements
    * we have two methods to deploy the environment.  
    * Method One: Full deployment environment by ourself
         - Install postgresql, pgAdmin and python3, we can download the installation package from the official website. 
         - According to the *Database environmental configuration*, create database, user, role, and import the data.
    * Method Two: use vagrant
         - Install virtual machine, VirtualBox. [download](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
         - Install Vagrant. [download](https://www.vagrantup.com/downloads.html)
         - Download the VM configuration. [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip), 
        then create vagrant dir, put it in, and run the command vagrant up.
        When vagrant up is finished running, you will get your shell prompts back. 
        At this point, you can run vagrant ssh to log in to your newly installed Linux VM!
         - Running the database
         - [Download data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), and put this file into the vagrant directory
         - cd into the vagrant directory and use the command psql -d news -f newsdata.sql. it can import the data to the new database.

* DataBase environmental configuration
    1. Create database news
    2. Create user: create user vagrant with password 'xxxxxx'
    3. Create role: create role vagrant LOGIN
    4. Import the data into the database, execute newsdata.sql: 
        - psql -d news -f newsdata.sql -U vagrant 
        - Execute newsdata.sql could create three tables: articles, authors, log. And insert the data. 
            - The authors table includes information about the authors of articles.
            - The articles table includes the articles themselves.
            - The log table includes one entry for each time a user has accessed the site, and read the articles.

* Code description
    - log_analysis.py has an execute function. It is used to connect to database and execute sql. Then we solved three questions through call this function.
        - What are the most popular three articles of all time? 
        - Who are the most popular article authors of all time? 
        - On which days did more than 1% of request lead to errors?
    - we should use idle to run this log_analysis.py in window, or execute python ./log_analysis.py in linux,  then it will generate a result.txt which printed out the three question result.
