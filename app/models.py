import sqlite3 as sql


def insert_account_holder(email,username,phone,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account_holder (email,username,phone,password) VALUES (?,?,?,?)" [email,username,phone,password])
    con.commit()
    con.close()

def insert_contact(name,phone,username,email):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO contact (name,phone,username,email) VALUES (?,?,?,?)" [name,phone,username,email])
    con.commit()
    con.close()
