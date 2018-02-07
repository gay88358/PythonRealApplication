class OrderData:
    def __init__(self, orderId, customerId):
        self._orderId = orderId
        self._customerId = customerId
    
    def orderId(self):
        return self._orderId

    def customerId(self):
        return self._customerId
