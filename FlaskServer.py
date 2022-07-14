from urllib import response
from time import sleep

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
global etherium
global bitcoin
global cat
global book
global mv
global cel
global dodge
global Tether
global sand
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
        cursor.execute(sql,(newPass,p.id))

        conn.commit()
    except:
        conn.rollback()
    conn.close()
    return render_template('login.html')


@app.route('/return', methods=['GET', 'POST'])
def returnProfile():
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
    global etherium
    global bitcoin
    global cat
    global book
    global mv
    global cel
    global dodge
    global Tether
    global sand

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
    coinList = []
    Coin = bitcoinMonitor()
    time.sleep(2.5)
    Coin1 = EteriumMonitor()
    time.sleep(2.5)

    Coin2 = DodgecoinMonitor()
    time.sleep(2.5)

    Coin3 = TetherMonitor()
    time.sleep(2.5)

    Coin4 = CatGirlMonitor()
    time.sleep(2.5)

    Coin5 = CelsiusMonitor()
    time.sleep(2.5)

    Coin6 = BitbookMonitor()
    time.sleep(2.5)

    Coin7 = SandboxMonitor()
    time.sleep(2.5)

    Coin8 = M7v2Monitor()
    time.sleep(2.5)

    Coin.type = typeTrim(Coin.type)
    Coin1.type = typeTrim(Coin1.type)
    Coin2.type = typeTrim(Coin2.type)
    Coin3.type = typeTrim(Coin3.type)
    Coin4.type = typeTrim(Coin4.type)
    Coin5.type = typeTrim(Coin5.type)
    Coin6.type = "BitBook"
    Coin7.type = "The Sandbox"
    Coin8.type = "M7v2"
    sand = Coin7.price
    book = Coin6.price
    mv = Coin8.price
    bitcoin = Coin.price
    etherium = Coin1.price
    dodge = Coin2.price
    Tether = Coin3.price
    cat = Coin4.price
    cel = Coin5.price

    coinList.append(Coin)
    coinList.append(Coin1)
    coinList.append(Coin2)
    coinList.append(Coin3)
    coinList.append(Coin4)
    coinList.append(Coin5)
    coinList.append(Coin6)
    coinList.append(Coin7)
    coinList.append(Coin8)
    print("here")

    return render_template('home.html')

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

@app.route('/purchase', methods=['GET', 'POST'])
def purchase():

    if request.method == 'POST':
        id = p.id
        money = 0
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
        if cryptoCoin == "Bitcoin":
            money = bitcoin
        if cryptoCoin == "Ethereum":
            money = etherium
        if cryptoCoin == "Dodgecoin":
            money = dodge
        if cryptoCoin == "Tether":
            money = Tether
        if cryptoCoin == "CatGirl":
            money = cat
        if cryptoCoin == "Celsius":
            money = cel
        if cryptoCoin == "Bitbook":
            money = book
        if cryptoCoin == "Sandbox":
            money = sand
        if cryptoCoin == "M7v2":
            money = mv
        z = money.replace("$", "")
        m = z.replace(",","")
        moneySpent = float(m)
        moneySpent = moneySpent * purchaseTotal

        if int(profile.money) - float(moneySpent) < 0:
            return render_template('Error.html')
        if float(moneySpent) > int(profile.money):
            return render_template('Error.html')
        else:
            profile.money = float(profile.money - moneySpent)
            cursor.execute('UPDATE profile set totalcoins = %s where id = %s', (newCoins, id))
            conn.commit()
            sql = "INSERT INTO `crypto` (`id`, `cost`, `type`) VALUES (%s, %s, %s)"

            cursor.execute(sql, (id, moneySpent, cryptoCoin))

            conn.commit()
            cursor.execute('UPDATE profile set money = %s where id = %s', (profile.money, id))
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
            return render_template('success.html')


@app.route('/login', methods=['GET', 'POST'])
def home():
    global etherium
    global bitcoin
    global cat
    global book
    global mv
    global cel
    global dodge
    global Tether
    global sand
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

        account = cursor.fetchone()
        cursor.execute('SELECT * FROM profile WHERE id = %s ', (account['id']))

        account1 = cursor.fetchone()
        prof = Profile(account1['id'], account1['money'], account1['totalcoins'])
        g.profile = prof
        setProfile(prof)
        coinList = []
        Coin = bitcoinMonitor()
        time.sleep(2.5)
        Coin1 = EteriumMonitor()
        time.sleep(2.5)


        Coin2 = DodgecoinMonitor()
        time.sleep(2.5)

        Coin3 = TetherMonitor()
        time.sleep(2.5)

        Coin4 = CatGirlMonitor()
        time.sleep(2.5)

        Coin5 = CelsiusMonitor()
        time.sleep(2.5)

        Coin6 = BitbookMonitor()
        time.sleep(2.5)

        Coin7 = SandboxMonitor()
        time.sleep(2.5)

        Coin8 = M7v2Monitor()
        time.sleep(2.5)


        Coin.type = typeTrim(Coin.type)
        Coin1.type = typeTrim(Coin1.type)
        Coin2.type = typeTrim(Coin2.type)
        Coin3.type = typeTrim(Coin3.type)
        Coin4.type = typeTrim(Coin4.type)
        Coin5.type = typeTrim(Coin5.type)
        Coin6.type = "BitBook"
        Coin7.type = "The Sandbox"
        Coin8.type = "M7v2"
        sand = Coin7.price
        book = Coin6.price
        mv = Coin8.price
        bitcoin = Coin.price
        etherium = Coin1.price
        dodge = Coin2.price
        Tether = Coin3.price
        cat = Coin4.price
        cel = Coin5.price






        coinList.append(Coin)
        coinList.append(Coin1)
        coinList.append(Coin2)
        coinList.append(Coin3)
        coinList.append(Coin4)
        coinList.append(Coin5)
        coinList.append(Coin6)
        coinList.append(Coin7)
        coinList.append(Coin8)


        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            return render_template("home.html", len=len(coinList), coinList=coinList)
        else:
            msg = 'Incorrect username/password!'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html', msg='')

def priceBitcoin():
    w = Webscrape()
    price = w.priceBitcoin()
    return price
def priceEthe():
    w = Webscrape()
    price = w.priceEterium()
    return price
def priceCat():
    w = Webscrape()
    price = w.priceCatGirl()
    return price
def priceCel():
    w = Webscrape()
    price = w.priceCelsius()
    return price
def priceMv():
    w = Webscrape()
    price = w.priceM7v2()
    return price
def priceThe():
    w = Webscrape()
    price = w.priceTether()
    return price
def priceSand():
    w = Webscrape()
    price = w.priceSandbox()
    return price
def priceBook():
    w = Webscrape()
    price = w.priceBitbook()
    return price

def priceDodge():
    w = Webscrape(0,"none","none",0,"none")
    price = w.priceDodgecoin()
    return price
def bitcoinMonitor():
    w = Webscrape(0,"none","none",0,"none")
    x = w.priceTrackBitcoin()
    coin = CoinDTO(x.price, x.type, x.trendIndicator, x.trendNum, x.source)
    print("here")
    return coin
def EteriumMonitor():
    w = Webscrape(0,"none","none",0,"none")
    x = w.priceTrackEthereum()
    coin = CoinDTO(x.price, x.type, x.trendIndicator, x.trendNum, x.source)
    return coin
def DodgecoinMonitor():
    w = Webscrape(0,"none","none",0,"none")
    x = w.priceTrackDodgecoin()
    coin = CoinDTO(x.price, x.type, x.trendIndicator, x.trendNum, x.source)
    return coin
def TetherMonitor():
    w = Webscrape(0,"none","none",0,"none")
    x = w.priceTrackTether()
    coin = CoinDTO(x.price, x.type, x.trendIndicator, x.trendNum, x.source)
    return coin
def CatGirlMonitor():
    w = Webscrape(0,"none","none",0,"none")
    x = w.priceTrackCatGirl()
    coin = CoinDTO(x.price, x.type, x.trendIndicator, x.trendNum, x.source)
    return coin
def CelsiusMonitor():
    w = Webscrape(0,"none","none",0,"none")
    x = w.priceTrackCelsius()
    coin = CoinDTO(x.price, x.type, x.trendIndicator, x.trendNum, x.source)
    return coin
def BitbookMonitor():
    w = Webscrape(0,"none","none",0,"none")
    x = w.priceTrackBitbook()
    coin = CoinDTO(x.price, x.type, x.trendIndicator, x.trendNum, x.source)
    return coin
def SandboxMonitor():
    w = Webscrape(0,"none","none",0,"none")
    x = w.priceTrackSandbox()
    coin = CoinDTO(x.price, x.type, x.trendIndicator, x.trendNum, x.source)
    return coin
def M7v2Monitor():
    w = Webscrape(0,"none","none",0,"none")
    x = w.priceTrackM7v2()
    coin = CoinDTO(x.price, x.type, x.trendIndicator, x.trendNum, x.source)
    print("final")
    return coin

def typeTrim(type):
    capitalCount = 0
    newType = ""
    for i in type:
        if i.isupper():
            capitalCount = capitalCount + 1
        if capitalCount > 1:
            break
        newType = newType + i
    return newType
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

        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"



        cursor.execute(sql, (email, password))

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