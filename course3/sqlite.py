import sqlite3


# create table: create table if not exists store(item text, quantity integer, price real)
# insert table: insert into store values(..., ..., ...)
# delete table: delete from store where item=?", (item, )
# update table: update store set quantity = ?, price = ? where item=?", (quantity, price, item)

def create_table():
    conn = sqlite3.connect("lite.db") # connect to database
    cur = conn.cursor() # 得到cursor用來操在資料庫
    cur.execute("create table if not exists store(item text, quantity integer, price real)")
    conn.commit() # commit 去資料庫，資料庫才會更新
    conn.close() # 關閉連線

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("delete from store where item=?", (item, ))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("update store set quantity = ?, price = ? where item=?", (quantity, price, item))
    conn.commit()
    conn.close()


print(view())