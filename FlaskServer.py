from flask import Flask, jsonify, abort, request, make_response, url_for, session, render_template, redirect

import os
import time
import datetime
import json
# import MySQLdb
import pymysql
# from flask_mysqldb import MySQL
app = Flask(__name__)
DB_USERNAME = 'root'
DB_PASSWORD = 'password'
DB_NAME = 'paperTrade'

@app.route('/')
def index():
    return render_template('login.html')

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
    app.run(debug=True)