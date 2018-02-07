from product import Product
class ProductImp(Product):
    def __init__(self, sku, name, price):
        Product.__init__(self)
        self._sku = sku
        self._name = name
        self._price = price
