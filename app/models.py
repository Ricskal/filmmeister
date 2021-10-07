from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    event_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    meister_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(4000), index=True, unique=True)
    year = db.Column(db.Integer, index=True, unique=True)
    length_minute = db.Column(db.Integer, index=True, unique=True)
    rating = db.Column(db.Float, index=True, unique=True)

    def __repr__(self):
        return '<Movie {}>'.format(self.title)
