from urllib import response

from flask import Flask, jsonify, abort, request, make_response, url_for, session, flash
from flask import render_template, redirect, g
from flask_session import Session
from src.paperTrade.webScraper import Webscrape
import pymysql
from src.paperTrade.DTO.profileDTO import Profile
from src.paperTrade.DTO.userDTO import User
from src.paperTrade.DTO.coinDTO import CoinDTO
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

p = Profile
users = []
def setProfile( Profile):
    p.money = Profile.money
    p.id = Profile.id
    p.totalcoins = Profile.totalcoins

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/newPassword', methods=['GET', 'POST'])
def newPass():
    newPass=request.form['newpassword']
    conn = pymysql.connect(host="localhost",
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "UPDATE `users` set password =  (`password`) where id = (`id`) VALUES (%s, %s)"
    try:
        # Execute the SQL command
        cursor.execute(sql,(newPass,p.id))

        # Commit your changes in the database
        conn.commit()
    except:
        # Rollback in case there is any error
        conn.rollback()
    # Executing the query
    conn.close()
    return render_template('login.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    id = p.id
    conn = pymysql.connect(host="localhost",
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute('SELECT * FROM profile WHERE id = %s ', id)

    account = cursor.fetchone()
    profile = Profile(account['id'], account['money'], account['totalcoins'])
    g.profile = profile
    cursor.execute('SELECT * FROM users WHERE id = %s ', id)

    account1 = cursor.fetchone()
    user = User(account1['id'], account1['email'], account1['password'])
    g.user = user

    return render_template('profile.html')

@app.route('/home')
def homePage():

    id = p.id
    conn = pymysql.connect(host="localhost",
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute('SELECT * FROM profile WHERE id = %s ', id)

    account = cursor.fetchone()
    cursor.execute('SELECT * FROM users WHERE id = %s ', id)

    account1 = cursor.fetchone()
    profile = Profile(account['id'], account['money'], account['totalcoins'])
    g.profile = profile
    email2 = ""
    for i in range(0, len(account1['email'])):
        if (account1['email'][i] == '@'):
            email2 = account1['email'][:i]
    user = User(account['id'], email2, "hd")
    g.user = user
    return render_template('home.html')

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':
        id = p.id
        purchaseTotal = request.form['purchaseAmt']
        cryptoCoin = request.form['coin']
        conn = pymysql.connect(host="localhost",
                               user=DB_USERNAME,
                               passwd=DB_PASSWORD,
                               db=DB_NAME,
                               port=3306)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM profile WHERE id = %s ', id)
        account = cursor.fetchone()
        profile = Profile(account['id'], account['money'], account['totalcoins'])
        purchaseTotal = float(purchaseTotal)
        profile.totalcoins = float(profile.totalcoins)
        newCoins = float(purchaseTotal+profile.totalcoins)
        money = profile.money-10
        cursor.execute('UPDATE profile set totalcoins = %s where id = %s', (newCoins, profile.id))
        conn.commit()
        sql = "INSERT INTO `crypto` (`id`, `cost`, `type`) VALUES (%s, %s, %s)"

        cursor.execute(sql, (id, money, cryptoCoin))

        conn.commit()

        cursor.execute('SELECT * FROM users WHERE id = %s ', id)
        account1 = cursor.fetchone()
        user = User(account1['id'], account1['email'], account1['password'])
        profile = Profile(account['id'], account['money'], account['totalcoins'])
        user = User(id, user.email, user.password)
        email2 = ""
        for i in range(0, len(user.email)):
            if (user.email[i] == '@'):
                email2 = user.email[:i]

        user.email = email2
        g.user = user
        g.profile = profile
        return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def home():
    email = request.form['email']
    password = request.form['password']
    conn = pymysql.connect(host="localhost",
                           user=DB_USERNAME,
                           passwd=DB_PASSWORD,
                           db=DB_NAME,
                           port=3306)
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password,))
    acc = cursor.fetchone()

    # if 'loggedin' in session.keys() and session['loggedin']:
    #     session.pop('id', None)
    #     email = request.form['email']
    #     user = User(0,email,"hafd")
    #     email2 = ""
    #     for i in range(0, len(user.email)):
    #         if (user.email[i] == '@'):
    #             email2 = user.email[:i]
    #
    #     user.email = email2
    #     g.user = user
    #     return render_template('home.html')
    if request.method == 'POST' and acc :

        g.profile = p
        email = request.form['email']
        password = request.form['password']
        user = User(0, email, password)
        email2 = ""
        for i in range(0, len(user.email)):
            if (user.email[i] == '@'):
                email2 = user.email[:i]

        user.email = email2
        g.user = user

        conn = pymysql.connect(host="localhost",
                               user=DB_USERNAME,
                               passwd=DB_PASSWORD,
                               db=DB_NAME,
                               port=3306)
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password,))

        # Fetch one record and return result

        # Fetch one record and return result
        account = cursor.fetchone()
        cursor.execute('SELECT * FROM profile WHERE id = %s ', (account['id']))

        account1 = cursor.fetchone()
        prof = Profile(account1['id'], account1['money'], account1['totalcoins'])
        g.profile = prof
        setProfile(prof)
        # w = Webscrape()
        # price = w.priceBitcoin()
        # type = w.typeBitcoin()
        # trendIndicator = w.trendIndicatorBitcoin()
        # trendNumber = w.trendNumberBitcoin()
        # image = w.sourceBitcoin()
        # coin = CoinDTO(price, type, trendIndicator, trendNumber, image)
        # g.coin = coin

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
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password,))
        cursor.execute('SELECT * FROM users WHERE email = %s ', email)
        account1 = cursor.fetchone()
        if account1:

            return render_template('login.html')
        # Create a new record

        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"



        # Execute the query
        cursor.execute(sql, (email, password))

        # the connection is not autocommited by default. So we must commit to save our changes.
        conn.commit()
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password,))
        account = cursor.fetchone()
        id = account['id']
        money = 10000
        totalcoins = 0
        profile = Profile(id,money,totalcoins)
        setProfile(profile)
        sql2 = "INSERT INTO `profile` (id,money, totalcoins) VALUES (%s,%s, %s)"
        cursor.execute(sql2, (id, money, totalcoins))

        # the connection is not autocommited by default. So we must commit to save our changes.
        conn.commit()
        return redirect('/')

    else:
        return render_template('register.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':

        flash('You were logged out.')

        return render_template('login.html')

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.secret_key = 'superSecretKey'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    app.debug = True
    app.run()