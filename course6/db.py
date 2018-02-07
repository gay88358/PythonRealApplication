import sqlite3
from productData import ProductData

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('order.db')
        self.cur = self.conn.cursor()
        self.cur.execute("create table if not exists customer (customerId integer primary key)")
        #self.cur.execute("create table if not exists order (orderId integer primary key, customerId integer, FOREIGN KEY(customerId) REFERENCES customer(customerId))")
        self.cur.execute("create table if not exists product (sku interger primary key, name text, price real)")
        #self.cur.execute("create table if not exists item (orderId integer sku integer, qty integer)")

        self.conn.commit()

    def __del__(self): #destructor
        self.conn.close()

    def storeProduct(self, pd):
        self.cur.execute("insert into product values(?, ?, ?)", (pd.sku(), pd.name(), pd.price()))
        self.conn.commit()

    def getProductData(self, sku):
        self.cur.execute("select * from product where sku = ?", (sku, ))
        rows = self.cur.fetchall()
        retrievedSku = rows[0][0]
        retrievedName = rows[0][1]
        retrievedPrice = rows[0][2]
        productData = ProductData(retrievedName, retrievedPrice, retrievedSku)
        return productData
        
    def deleteProduct(self, sku):
        self.cur.execute("delete from product where sku = ?", (sku, ))
        self.conn.commit()

    def showAllProduct(self):
        self.cur.execute("select * from product")
        rows = self.cur.fetchall()
        for row in rows:
            print("Product {}, name = {}, price = {}".format(row[0], row[1], row[2]))

    def clear(self):
        self.cur.execute("delete from product")
        self.conn.commit()    


db = DB()
db.showAllProduct()