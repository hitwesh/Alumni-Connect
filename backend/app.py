from flask import Flask, render_template, request, redirect, url_for, flash, session
import csv
import os
import pandas as pd

# Import configuration
from config import Config
from model import recommend_mentors as recommend_mentors_from_model

# Configure template and static folders to point to frontend directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'frontend', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, '..', 'frontend', 'static')

# Initialize Flask app with template and static folder configuration
app = Flask(__name__, 
           template_folder=TEMPLATE_DIR,
           static_folder=STATIC_DIR,
           static_url_path='/static')

# Apply configuration
app.config.from_object(Config)

# Configure session security
if app.config['FLASK_ENV'] == 'production':
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax'
    )

# Configure production settings
if os.environ.get('FLASK_ENV') == 'production':
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Data files live under ../database
DATA_DIR = os.path.join(BASE_DIR, '..', 'database')
USER_FILE = os.path.join(DATA_DIR, 'users.csv')
ALUMNI_FILE = os.path.join(DATA_DIR, 'alumni_dataset.csv')

def init_files():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'email', 'password', 'role'])
            writer.writeheader()

    if not os.path.exists(ALUMNI_FILE):
        with open(ALUMNI_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'email', 'batch', 'department', 'skills'])
            writer.writeheader()

init_files()

def load_alumni_data():
    if os.path.exists(ALUMNI_FILE):
        df = pd.read_csv(ALUMNI_FILE)
        df.fillna('', inplace=True) # Convert NaN to empty strings
        return df
    return pd.DataFrame(columns=['name','email','batch','department','skills'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # use .get() with defaults to avoid KeyError when a field is missing
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        role = request.form.get('role', 'student').strip() or 'student'

        # defensive read: use .get on row dicts in case headers are unexpected
        if os.path.exists(USER_FILE):
            with open(USER_FILE, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if (row.get('email') or '').strip().lower() == email.lower():
                        flash('Email already registered!', 'danger')
                        return redirect(url_for('login'))

        with open(USER_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['name','email','password','role'])
            writer.writerow({'name': name, 'email': email, 'password': password, 'role': role})

        if (role or '').lower() == 'alumni':
            with open(ALUMNI_FILE, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['name','email','batch','department','skills'])
                writer.writerow({'name': name, 'email': email, 'batch': 'Not Provided', 'department': 'Not Provided', 'skills': 'Not Provided'})

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        if os.path.exists(USER_FILE):
            with open(USER_FILE, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # defensive access using .get()
                    if (row.get('email') or '').strip().lower() == email.lower() and (row.get('password') or '').strip() == password:
                        # normalize session user to always contain name/email/role keys
                        session['user'] = {
                            'name': row.get('name', ''),
                            'email': row.get('email', ''),
                            'role': row.get('role', 'student')
                        }
                        print(session['user'])
                        flash(f"Welcome {session['user'].get('name','')}!", 'success')
                        return redirect(url_for('dashboard'))
        flash('Invalid credentials.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please login first.', 'warning')
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/alumni', methods=['GET', 'POST'])
def alumni():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        batch = request.form['batch']
        department = request.form['department']
        skills = request.form['skills']

        with open(ALUMNI_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['name','email','batch','department','skills'])
            writer.writerow({'name': name, 'email': email, 'batch': batch, 'department': department, 'skills': skills})

        flash('Alumni added successfully!', 'success')

    alumni_list = []
    with open(ALUMNI_FILE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            alumni_list.append(row)

    return render_template('alumni.html', alumni=alumni_list)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    mentors = []
    if request.method == 'POST':
        # accept either 'interest' (old) or 'interests' (template)
        interest = request.form.get('interest') or request.form.get('interests', '')
        interest = (interest or '').strip()
        print('Interest submitted:', interest)
        if interest:
            alumni_df = load_alumni_data()
            mentors = recommend_mentors_from_model(interest, alumni_df)
            print(mentors)
    return render_template('recommend.html', mentors=mentors)

if __name__ == '__main__':
    app.run(debug=True)
