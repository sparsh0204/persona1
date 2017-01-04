import sqlite3 as sql

def insertUser(username,password,age):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password,age) VALUES (?,?,?)", (username,password,age))
    con.commit()
    con.close()

def retrieveUsers(username):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT password FROM users WHERE username LIKE ?", (username,))
    users = cur.fetchall()
    con.close()
    return users

def allusernames():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT username FROM users")
    users = cur.fetchall()
    con.close()
    return users
