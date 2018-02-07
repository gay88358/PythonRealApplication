import sqlite3


# connect 
# cursor
# execute sql
# commit
# close

def connect():
    conn = sqlite3.connect("book.db")
    # connect to the database
    cur = conn.cursor()
    # get cursor of database
    cur.execute("create table if not exists book (id integer primary key, title text, author text, year integer, isbn integer)")
    # execute sql
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("insert into book values(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("select * from book")
    rows = cur.fetchall()
    conn.close()
    return rows

def getBookById(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("select * from book where id = ?", (id, ))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("delete from book where id = ?", (id, ))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("update book set title = ?, author = ?, year = ?, isbn = ? where id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

def search(title):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("select * from book where title = ?", (title, ))
    row = cur.fetchall()
    conn.close()
    return row


# list [ ] 
# dict { }
# tuple ()

print(view())

print(search('The beef'))





