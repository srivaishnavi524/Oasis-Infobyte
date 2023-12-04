from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret_key'

users = {}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return 'Username already taken. Choose a different one.'

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        users[username] = {'username': username, 'password': hashed_password}

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/')
def home():
    reg_link = url_for('register')
    return f'Welcome to the Home Page! For register <a href="{reg_link}">Register</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            if check_password_hash(users[username]['password'], password):
                session['username'] = username
                return redirect(url_for('secured_page'))
        return 'Invalid username or password. Please try again.'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/secured_page')
def secured_page():
    if 'username' in session:
        username = session['username']
        logout_link = url_for('logout')
        return f'Hello, {username}! This is the secured page. <a href="{logout_link}">Logout</a>'
    else:
        return 'You are not logged in. Please log in first.'
if __name__ == '__main__':
    app.run(debug=True)
