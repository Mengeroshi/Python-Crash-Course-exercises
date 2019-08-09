sandwich_orders = ["rosbif", "pastrani", "sailor", "runza"]
finished_sanwiches = []

while  sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f"I made a {made_sandwich} sandwich")

    finished_sanwiches.append(made_sandwich)

print("\nFinished Sanwiches:")
for sandwich in finished_sanwiches:
    print(sandwich)