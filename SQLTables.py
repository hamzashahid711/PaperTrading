import pymysql
DB_USERNAME = 'root'
DB_PASSWORD = 'password'
DB_NAME = 'paperTrade'

conn = pymysql.connect(host = "localhost",
                       user = DB_USERNAME,
                       passwd = DB_PASSWORD,
                       db = DB_NAME,
                       port = 3306)

cursor = conn.cursor()
cursor.execute("SELECT VERSION()")

cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, "
               "email VARCHAR(255), "
               "password VARCHAR(255))")
cursor.execute("CREATE TABLE profile (id INT PRIMARY KEY, "
               "money INT, "
               "totalShares INT)")
cursor.execute("CREATE TABLE stocks (id INT PRIMARY KEY, "
               "cost FLOAT, "
               "type VARCHAR(255),"
               "totalCoinsBought FLOAT)")

cursor.close()
conn.close()
