import sqlite3

user_db = sqlite3.connect("./user.db")
cursor = user_db.cursor()
cursor.execute("drop table users")
cursor.execute("create table users(user varchar(16), pwd varchar(64))")
user_db.commit()


