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

cursor.execute("create table users ( \
    email varchar(70) primary key not null,\
    password varchar(100) not null\
    );")



cursor.close()
conn.close()
