from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json

from flask import make_response
import requests

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///category.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "categories"


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    print (state)
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    # ya29.GltdBsFRzXflKhPk_xoJDopI5GEHEJR5rno8PIKrYQ7Lq1BwPW5HZ1u8QA3-GuUh7dJp31W8EjlM-e-SP71YWaPQbmIBiyLMxLHd2Dcwh_WzvImpHR_Ez-LpZqVe
    print(access_token)
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 501)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    print("gplus_id ", gplus_id)  # 114712143004133493014
    print(result['user_id'])     # 114712143004133493014
    # 45617886343-gclvapskt05tu1ik8u55tfpitfj20hfo.apps.googleusercontent.com
    print(result['issued_to'])

    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print ("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already \
                                connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()
    print(data)

    login_session['id'] = data['id']
    login_session['username'] = data['given_name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: \
150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    flash("you are now logged in as %s" % login_session['id'])
    print ("done!")
    return output


# User Helper Functions
def createUser(login_session):
    uid = str(login_session['id'])
    uname = str(login_session['username'])
    uemail = str(login_session['email'])
    upicture = str(login_session['picture'])

    newUser = User(id=uid, name=uname, email=uemail, picture=upicture)
    session.add(newUser)
    session.commit()
    return newUser.id


def deleteUser(login_session):
    session.query(User).filter_by(id=login_session['id']).delete()
    session.commit()


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    if 'username' in login_session:
        deleteUser(login_session)

    # print(login_session['username'])
    access_token = login_session.get('access_token')
    # print(access_token)

    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# Show all restaurants
@app.route('/')
@app.route('/catelog/')
def showCategories():
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Item).order_by(asc(Item.name))
    if 'username' not in login_session:
        return render_template('categories.html', items=items,
                               categories=categories)
    else:
        return render_template('publiccategories.html', items=items,
                               categories=categories)


@app.route('/catelog/JSON/')
def showCategoriesJson():
    categories = session.query(Category).order_by(asc(Category.name))
    return jsonify(categories=[c.serialize for c in categories])


# Create a new category
@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login')

    if request.method == 'POST':
        newCategory = Category(name=request.form['name'],
                               user_id=login_session['id'])
        session.add(newCategory)
        flash('New Category %s Successfully Created' % newCategory.name)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')


@app.route('/catelog/<int:category_id>/')
@app.route('/catelog/<int:category_id>/items/')
def showItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(
        cat_id=category_id).order_by(asc(Item.name))
    return render_template('showCategoryInfo.html', items=items,
                           category=category)


@app.route('/catelog/<int:category_id>/items/JSON')
def showItemsJson(category_id):
    items = session.query(Item).filter_by(
        cat_id=category_id).order_by(asc(Item.name))
    return jsonify(items=[i.serialize for i in items])


# Edit a category
@app.route('/catelog/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    if 'username' not in login_session:
        return redirect('/login')

    editedCategory = session.query(Category).filter_by(id=category_id).one()
    if login_session['id'] != editedCategory.user_id:
        return "you are non authorized to edit it."

    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category Successfully Edited %s' % editedCategory.name)
            return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('editCategory.html', category=editedCategory)


# Delete a category
@app.route('/catelog/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    if 'username' not in login_session:
        return redirect('/login')

    categoryToDelete = session.query(Category).filter_by(id=category_id).one()
    if login_session['id'] != categoryToDelete.user_id:
        return "you are non authorized to delete it."

    if request.method == 'POST':
        session.delete(categoryToDelete)
        flash('%s Successfully Deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('deleteCategory.html',
                               category=categoryToDelete)


# Create a new item
@app.route('/catelog/<int:category_id>/item/new/', methods=['GET', 'POST'])
def newItem(category_id):
    if 'username' not in login_session:
        return redirect('/login')

    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form[
            'description'], cat_id=category_id)
        session.add(newItem)
        session.commit()
        flash('New Menu %s Item Successfully Created' % (newItem.name))
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('newItem.html', category_id=category_id)


# Edit a menu item
@app.route('/catelog/<int:category_id>/item/<int:item_id>/edit', methods=[
    'GET', 'POST'])
def editItem(category_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')

    login_session['id'] = '100003'
    editedItem = session.query(Item).filter_by(id=item_id).one()
    if login_session['id'] != editedItem.category.user_id:
        return "you are non authorized to edit the item."

    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        flash('Menu Item Successfully Edited')
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('editItem.html', category_id=category_id,
                               item_id=item_id, item=editedItem)


# Delete a menu item
@app.route('/catelog/<int:category_id>/item/<int:item_id>/delete', methods=[
    'GET', 'POST'])
def deleteItem(category_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')

    # category = session.query(Category).filter_by(id=category_id).one()
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    if login_session['id'] != itemToDelete.category.user_id:
        return "you are non authorized to delete the item."

    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('deleteItem.html', item=itemToDelete)


@app.route('/catelog/item/<int:item_id>/JSON')
def showItemJson(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(item.serialize)


@app.route('/catelog/item/<int:item_id>/info')
def showItemInfo(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('showItemInfo.html', item=item)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    # app.run(host='0.0.0.0', port=5000)
    app.run()
