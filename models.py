import pymysql.cursors

def insertUser(username,password,age):
    con = pymysql.connect(host="localhost",user = "root",passwd = "qwertyy", db = "python")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password,age) VALUES (%s,%s,%s)", (username,password,age))
    con.commit()
    con.close()

def retrieveUsers(username):
    con = pymysql.connect(host="localhost",user = "root",passwd = "qwertyy", db = "python")
    cur = con.cursor()
    cur.execute("SELECT password FROM users WHERE username LIKE %s", (username,))
    users = cur.fetchall()
    con.close()
    return users

def allusernames():
    con = pymysql.connect(host="localhost",user = "root",passwd = "qwertyy", db = "python")
    cur = con.cursor()
    cur.execute("SELECT username FROM users")
    users = cur.fetchall()
    con.close()
    return users
