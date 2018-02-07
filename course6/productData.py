class ProductData:
    def __init__(self, name, price, sku):
        self._name = name
        self._price = price
        self._sku = sku
    
    def name(self):
        return self._name

    def price(self):
        return self._price
    
    def sku(self):
        return self._sku