from flask import Flask, jsonify, abort, request, make_response, url_for, session
from flask import render_template, redirect, g
from flask_session import Session
import pymysql
import os
import time
import datetime
import json
# import MySQLdb

# from flask_mysqldb import MySQL

app = Flask(__name__, static_url_path="")
sess = Session()
DB_USERNAME = 'root'
DB_PASSWORD = 'password'
DB_NAME = 'paperTrade'
app.secret_key = 'superSecretKey'

class User:
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User: {self.email}>'

users = []


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def home():
    if 'loggedin' in session.keys() and session['loggedin']:
        email = request.form['email']
        user = User(0,email,"hafd")
        email2 = ""
        for i in range(0, len(user.email)):
            if (user.email[i] == '@'):
                email2 = user.email[:i]

        user.email = email2
        g.user = user
        return render_template('home.html')
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        g.user.email = email

        conn = pymysql.connect(host="localhost",
                               user=DB_USERNAME,
                               passwd=DB_PASSWORD,
                               db=DB_NAME,
                               port=3306)
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password,))

        # Fetch one record and return result
        account = cursor.fetchone()

        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['email'] = account['email']
            # Redirect to home page
            return render_template('home.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html', msg='')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = pymysql.connect(host = "localhost",
                               user=DB_USERNAME,
                               passwd=DB_PASSWORD,
                               db=DB_NAME,
                               port=3306)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"

        # Execute the query
        cursor.execute(sql, (email, password))

        # the connection is not autocommited by default. So we must commit to save our changes.
        conn.commit()
        return redirect('/')

    else:
        return render_template('register.html')



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    app.debug = True
    app.run()