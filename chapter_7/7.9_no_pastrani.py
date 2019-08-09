sandwich_orders = ["pastrani","rosbif", "pastrani", "sailor", "runza", "pastrani"]
finished_sanwiches = []

print("Deli has run out the pastrani of menu")

while  "pastrani" in sandwich_orders:
    sandwich_orders.remove("pastrani")

print(sandwich_orders)