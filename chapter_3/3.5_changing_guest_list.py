guest_list = ['gerardo', 'fabian', 'hakeem']

print(f"Hi {guest_list[0]}, I would like to invite you to a dinner")
print(f"Hi {guest_list[1]}, I would like to invite you to a dinner")
print(f"Hi {guest_list[2]}, I would like to invite you to a dinner")

print(guest_list[2])

del guest_list[2]
guest_list.insert(2,"rolando")

print(f"Hi {guest_list[0]}, I would like to invite you to a dinner")
print(f"Hi {guest_list[1]}, I would like to invite you to a dinner")
print(f"Hi {guest_list[2]}, I would like to invite you to a dinner")