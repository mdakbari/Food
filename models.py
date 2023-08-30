from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Booking(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    datetime = db.Column(db.String, nullable=False)
    people = db.Column(db.Integer, nullable=False)
    msg = db.Column(db.String, nullable=False)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    subject = db.Column(db.String, nullable=False)
    msg = db.Column(db.String, nullable=False)
