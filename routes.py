from flask import render_template, request, flash, Blueprint
from models import Booking,Contact , db

main = Blueprint('main', __name__)

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
