from db import DB
from product import Product

class ProductProxy(Product):
    def __init__(self, sku):
        self._sku = sku
        self.db = DB()
    
    def price(self):
        p = self.db.getProductData(self._sku)
        return p.price()

    def name(self):
        p = self.db.getProductData(self._sku)
        return p.name()
        
    def sku(self):
        p = self.db.getProductData(self._sku)
        return p.sku()
        