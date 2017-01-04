from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
import pymysql.cursors
import models as dbhandler

app = Flask(__name__)

app.secret_key = 'jsdjmnsd5451'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    return render_template('login.html')  

@app.route('/welcome')
@login_required
def welcome():
	return render_template('welcome.html')
 

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            if str(dbhandler.retrieveUsers(request.form['username'])[0][0]) == request.form['password']:
                session['logged_in'] = True
                flash('Login successful.')
                return render_template('welcome.html')
            else:
                error = 'Invalid Credentials. Please try again.'
        except IndexError:
            error = 'User does not exists please register first'
            return render_template('login.html', error=error)
        
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		usr = dbhandler.allusernames()
		for u in usr:
			if u[0] == request.form['username']:
				flash('User already exists.')
				return render_template('signup.html')
		username = request.form['username']
		password = request.form['password']
		age = request.form['age']
		dbhandler.insertUser(username,password,age)
		flash('Register successful.')
		return render_template('signup.html')
	return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('Logout successful.')
    return redirect(url_for('login'))


if __name__ == '__main__':
	app.run()