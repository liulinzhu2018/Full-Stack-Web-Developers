from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///category.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# category for Soccer
category1 = Category(name="Soccer", user_id='100001')

session.add(category1)
session.commit()


item1 = Item(name="Two shinguards", description="xxx", category=category1)

session.add(item1)
session.commit()

item2 = Item(name="Shinguards", description="xxx",  category=category1)

session.add(item2)
session.commit()

item3 = Item(name="Soccer Cleats", description="xxx", category=category1)

session.add(item3)
session.commit()

item4 = Item(name="Jersey", description="xxx", category=category1)

session.add(item4)
session.commit()


# category for Hockey
category2 = Category(name="Hockey", user_id='100001')

session.add(category2)
session.commit()

item1 = Item(name="Stick", description="xxx", category=category2)

session.add(item1)
session.commit()

# category for Snowboarding
category3 = Category(name="Snowboarding", user_id='100003')

session.add(category3)
session.commit()

item1 = Item(name="Goggies", description="xxx", category=category3)

session.add(item1)
session.commit()

item2 = Item(name="Snowboard", description="xxx",  category=category3)

session.add(item2)
session.commit()


# categoryToDelete = session.query(Category).filter_by(id=2).one()
# session.delete(categoryToDelete)
# session.commit()


# u1 = User(id='1', name='lz', email='liulinzhu2018@gmail.com',
#          picture='https://lh4.googleusercontent.com/-TuivbJmIF-w/AAAAAAAAAAI/AAAAAAAAAAA/AGDgw-jOV055iMmyU_gGdZywgJmpbgLVyg/mo/photo.jpg')
# u2 = User(id='116310742707476762658123', name='test', email='liulinzhu',
#          picture='https://lh4.googleusercontent.com/-TuivbJmIF-w/AAAAAAAAAAI/AAAAAAAAAAA/AGDgw-jOV055iMmyU_gGdZywgJmpbgLVyg/mo/photo.jpg')


u1 = User(id='100001', name='a', email='a@163.com')
session.add(u1)
session.commit()

u2 = User(id='100002', name='b', email='b@163.com')
session.add(u1)
session.commit()

# session.query(User).filter_by(id=u1.id).delete()
# session.query(User).filter_by(id='116310742707476762658').delete()
# session.commit()

print ("finish!")
