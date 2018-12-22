# Project Categories
---
This project develop an application that provides a list of items within a variety of categories 
As well as provide a user registration and authentication system. 
Registered users will have the ability to post, edit and delete their own items.
 
# Usage
---
- 1.Install Vagrant and VirtualBox
- 2.Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
- 3.Launch the Vagrant VM (vagrant up)
- 4.Write our Flask application locally in the vagrant/catalog directory (which will automatically be synced to /vagrant/catalog within the VM).
- 5.Run our application within the VM (python /vagrant/catalog/application.py)
- 6.Access and test our application by visiting http://localhost:5000 locally

# Code description
---
## part 1 : python
+ datbase operation
	* database_setup.py use sqlalchemy to create a map from tables to objects.
    * we designed two tables, category and item.
	* category table consists of two columns, include id(primary key), name.
	* item table has five columns, include id(primary key), name, description, cat_id. cat_id is a foreign key for the item table, and a primary key for the category table.
	* lotsofitems.py use to crud through objects.
	* project.py is use flask framework to create a server. It opens 5000 port locally. It defines some app route.
	
+ Main page
	* '/' or '/catalog' is the main page. It lists all categories and items.
	* it connects with some pages, such as login.html, categories.html.
    
+ Login
	* '/login' page, implement a third-party authentication & authorization service, our can login in use google accounts.
	* now all page is public, we can also set authentication on some page, only login in user can read.
	
+ Category operation
	* '/category/new/ page use to create a category.
	* '/catelog/<int:category_id>/' or '/catelog/<int:category_id>/items' page show this category, and list all items of it.
	* '/catelog/<int:category_id>/items/JSON' page use json to list all items of this category.
	* '/catelog/<int:category_id>/edit/' page use to change a category. 
	* '/catelog/<int:category_id>/delete/' use to remove a category.
	
+ item operation
	* '/catelog/<int:category_id>/item/new/' page create a new item.
	* '/catelog/<int:category_id>/item/<int:item_id>/edit' page edit a item.
	* '/catelog/<int:category_id>/item/<int:item_id>/delete' page delete a item.
	* '/catelog/item/<int:item_id>/JSON' use json to display a item.
	* '/catelog/item/<int:item_id>/info' show a item detail infomation.
	
## part 2 : html
+ Main page
	* publiccategories.html, non logged users visited main page.
	* categories.html, login user access home page.
	* header.html
	* main.html
	
+ Login
* login.html, login in page.
	
+ Category page
	* newCategory.html
	* editCategory.html
	* deleteCategory.html
	* showCategoryInfo.html
	
+ Item page
	* newItem.html
	* editItem.html
	* deleteItem.html
	* showItemInfo.html
	
## part 3 : css
+ styles.css include all styles of this application.
+ css file must push in static directory.
+ static directory is also pushing some picture which this application page uses.
