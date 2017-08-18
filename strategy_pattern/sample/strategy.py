from strategy_abc import AbsStrategy


class ShippingCost(object):
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """
    def __init__(self, strategy):
        self._strategy = strategy

    def shipping_cost(self, order):
        return self._strategy.calculate(order)


class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        return 3.00


class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return 5.00


class UPSStrategy(AbsStrategy):
    def calculate(self, order):
        return 4.00


class Order(object):
    def __init__(self):
        pass
