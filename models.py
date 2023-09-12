from flask_sqlalchemy import SQLAlchemy
import bcrypt
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

class Foods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    category = db.Column(db.String(255))
    description = db.Column(db.Text)
    image = db.Column(db.String(255))

class Signup(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)
