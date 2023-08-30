# from  flask import Flask,redirect,url_for,render_template,request,flash
# import json
# from flask_sqlalchemy import SQLAlchemy




# app=Flask(__name__)

# with open('config.json', 'r') as c:
#     params = json.load(c)['params']
# local_server = True
# app = Flask(__name__)
# app.secret_key ="manthan"

# if(local_server):
#     app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
# else:
#     app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']

# db = SQLAlchemy(app)


# class Booking(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, nullable=False)
#     datetime = db.Column(db.String, nullable=False)
#     people = db.Column(db.Integer, nullable=False)
#     msg = db.Column(db.String, nullable=False)





# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('index.html')


# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/service')
# def service():
#     return render_template('service.html')

# @app.route('/menu')
# def menu():
#     return render_template('menu.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/booking', methods=['GET','POST'])
# def booking():
#     if (request.method == 'POST'):
#         name = request.form.get('name')
#         email = request.form.get('email')
#         datetime = request.form.get('datetime')
#         people = request.form.get('people')
#         msg = request.form.get('message')
#         conform = Booking(name=name, email=email, datetime=datetime, people=people, msg=msg)
#         db.session.add(conform)
#         db.session.commit()
#         flash('Booking is confirmed! Thank you for your reservation.', 'success')

#         return render_template('booking.html')
#     return render_template('booking.html')



# app.run(port=5000,debug=True)

from flask import Flask
from models import db
from routes import main
import json

app = Flask(__name__)
app.secret_key = "manthan"

with open('config.json', 'r') as c:
    params = json.load(c)['params']
local_server = True

if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']

db.init_app(app)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
