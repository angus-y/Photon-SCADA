import os
import threading
import bcrypt
import colorama
import modules.blynk_stream_retrieve as blynk_stream_retrieve
import modules.config as config
from flask import Flask, session, render_template, redirect, url_for, request, g

config.main()

# init hashes and color output
colorama.init()
with open('creds.txt', 'r') as f:
    username, password = f.read().split('\n')  # user : angus, pass : flaskbiggae
username = username.encode()
password = password.encode()

# init flask server
app = Flask(__name__)
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
        else:
            print ("\x1b[1m\x1b[33m[-]\x1b[0mDetected incorrect login")
            return render_template('login_failed.html')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if g.user:
        return render_template('index.html')
    return redirect(url_for('login'))


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


if __name__ == '__main__':
    # init data blynk streaming
    t = threading.Thread(target=blynk_stream_retrieve.main, args=())
    t.start()
    print('\x1b[1m\x1b[32m[+]\x1b[0mStarted Blynk data streamer')

    app.run(debug=True, host='0.0.0.0')
