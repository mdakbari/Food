from flask import render_template, request, flash, Blueprint
from models import Booking,Contact , db
import json
main = Blueprint('main', __name__)

with open('config.json', 'r') as c:
    params = json.load(c)['params']

@main.route('/')
@main.route('/home')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/service')
def service():
    return render_template('service.html')

@main.route('/menu')
def menu():
    return render_template('menu.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        msg = request.form.get('message')
        confirm = Contact(name=name, email=email, subject=subject, msg=msg)
        db.session.add(confirm)
        db.session.commit()
    return render_template('contact.html')

@main.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        datetime = request.form.get('datetime')
        people = request.form.get('people')
        msg = request.form.get('message')
        confirm = Booking(name=name, email=email, datetime=datetime, people=people, msg=msg)
        db.session.add(confirm)
        db.session.commit()
        flash('Booking is confirmed! Thank you for your reservation.', 'success')
        return render_template('booking.html')
    return render_template('booking.html')


@main.route("/admin")
def admin():
  
    return render_template("register.html")

@main.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        uname = request.form.get('uname')
        upassword = request.form.get('pass')

        if uname==params['admin_name'] and upassword==params['admin_password']:
            return render_template('admin.html')
    return render_template("login.html")
