from order import Order
class OrderImp(Order):
    def __init__(self, customerId):
        self._customerId = customerId
        self.items = []
        
    def addItem(self, p, qty):
        
    def total(self):
