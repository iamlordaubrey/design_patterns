from strategy import ShippingCost, FedExStrategy, PostalStrategy, UPSStrategy, Order

order = Order()
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)

cost = cost_calculator.shipping_cost(order)
assert cost == 3.00


order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)

cost = cost_calculator.shipping_cost(order)
assert cost == 5.00


order = Order()
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)

cost = cost_calculator.shipping_cost(order)
assert cost == 4.00


print("Test passed")
