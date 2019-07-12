import os
import bcrypt
import blynklib
import colorama
from flask import Flask, session, render_template, redirect, url_for, request, g

auth_token = ''
blynk = blynklib.Blynk(auth_token)
colorama.init()
with open('creds.txt', 'r') as f:
    username, password = f.read().split('\n')  # user : angus, pass : flaskbiggae
username = username.encode()
password = password.encode()

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(24)


@app.route('/')
def redirec_from_root():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        session.pop('user', None)
        username_inp = request.form['username'].encode()
        password_inp = request.form['password'].encode()
        if bcrypt.checkpw(username_inp, username) and bcrypt.checkpw(password_inp, password):
            session['user'] = request.form['username']
            return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if g.user:
        return render_template('dashboard.html')
    return redirect(url_for('login'))


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
