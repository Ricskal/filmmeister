#from filmmeister import app_inst
#print(app_inst.config['SECRET_KEY'])

from app import db
from app.models import User, Movie

#u = User(username='jeMoeder2', email='Moeder2@jouw.de')
#db.session.add(u)
#db.session.commit()

users = User.query.all()
print(users)
for u in users: print(u.id, u.username)

#u = User.query.get(1)
#p = Movie(title='tenet', meister=u)
#db.session.add(p)
#db.session.commit()

#get all posts written by a user
#u = User.query.get(1)
#print(u)
#
#movie = u.meister_rel.all()
#print(movie)

# print post author and body for all posts
#movie = Movie.query.all()
#for m in movie:
#    print(m.id, m.meister.username, m.title)
#
#
#users = User.query.all()
#for u in users:
#    db.session.delete(u)
#
#posts = Movie.query.all()
#for p in posts:
#    db.session.delete(p)
#
#db.session.commit()