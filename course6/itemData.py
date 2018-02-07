from product import Product

class ItemData:
    def __init__(self, orderId, qty, sku):
        self._orderId = orderId
        self._qty = qty
        self._sku = sku

    def orderId(self):
        return self._orderId
    
    def qty(self):
        return self._qty
    
    def sku(self):
        return self._sku

