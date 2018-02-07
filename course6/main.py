import unittest

from product import Product
from productData import ProductData
from productProxy import ProductProxy
from item import Item
from order import Order
from db import DB
class TestOrderMethod(unittest.TestCase):

    def test_db(self):
        db = DB()
        productData = ProductData("apple", 20, 0)
        db.storeProduct(productData)
        retreiveProductData = db.getProductData(0)
        db.deleteProduct(0)
        self.assertEqual(productData.name(), retreiveProductData.name())
        self.assertEqual(productData.price(), retreiveProductData.price())
        self.assertEqual(productData.sku(), retreiveProductData.sku())

    def test_productProxy(self):
        db = DB()
        productData = ProductData("apple", 20, 0)
        db.storeProduct(productData)
        p = ProductProxy(0)
        self.assertEqual(productData.name(), p.name())
        self.assertEqual(productData.price(), p.price())
        self.assertEqual(productData.sku(), p.sku())        
        db.deleteProduct(0)

    #def test_orderProxy(self):

if __name__ == '__main__':
    db = DB()
    db.clear()
    unittest.main()
