from flask import render_template, request, flash, Blueprint,session,redirect,Flask
from models import Booking,Contact,Foods, Signup, db
from werkzeug.utils import secure_filename
import json
import os
import bcrypt

app = Flask(__name__)
main = Blueprint('main', __name__)


with open('config.json', 'r') as c:
    params = json.load(c)['params']

app.config['UPLOAD_FOLDER'] = params['file_upload']


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
    categories = db.session.query(Foods.category).distinct().all()
    selected_category = request.args.get('category', 'Breakfast')
    menu_items = Foods.query.filter_by(category=selected_category).all()

    return render_template('menu.html', menu_items=menu_items, categories=categories, selected_category=selected_category)

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


#  Admin Route

@main.route("/signup", methods=['GET','POST'])
def signup():
    if (request.method == 'POST'):
        uname = request.form.get('uname')
        email = request.form.get('email')
        password = request.form.get('pass')
        new_user = Signup(uname=uname,email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')



@main.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        uname = request.form.get('uname')
        upassword = request.form.get('pass')
        user = Signup.query.filter_by(uname=uname).first()
        
        # if uname==params['admin_name'] and upassword==params['admin_password']:
        #     session['user'] = uname

        if user and bcrypt.checkpw(upassword.encode('utf-8'), user.password.encode('utf-8')):
            return render_template('admin_booking.html')
        return render_template("login.html")
    
    return render_template("login.html")

@main.route("/admin")
def admin():
    return render_template("register.html")

@main.route("/admin_booking")
def admin_booking():
    if 'user' not in session:
        return redirect("login.html")
    book = Booking.query.all()
    return render_template("admin_booking.html", book=book)

@main.route("/admin_contact")
def admin_contact():
    if 'user' not in session:
        return redirect("login.html")
    contact = Contact.query.all()
    return render_template("admin_contact.html", contact=contact)

@main.route("/admin_menu", methods=['GET','POST'])
def admin_menu():
    if 'user' not in session:
        return redirect("login.html")
    
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])  
        description = request.form['description']
        category = request.form['category']
        image_file = request.files['image']  

        if image_file:
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = None
        new_food = Foods(name=name, price=price, category=category, description=description, image=filename)
        db.session.add(new_food)
        db.session.commit()
        return render_template("admin_menu.html")
    food = Foods.query.all()
    return render_template("admin_menu.html",  food=food)
