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

print("\nHey people, I found a bigger dinner table \n")

guest_list.insert(0, "gloria")
guest_list.insert(2, "manuel")
guest_list.append("omar")

print(f"Hi {guest_list[0]}, I would like to invite you to a dinner")
print(f"Hi {guest_list[1]}, I would like to invite you to a dinner")
print(f"Hi {guest_list[2]}, I would like to invite you to a dinner")
print(f"Hi {guest_list[3]}, I would like to invite you to a dinner")
print(f"Hi {guest_list[4]}, I would like to invite you to a dinner")
print(f"Hi {guest_list[5]}, I would like to invite you to a dinner")

print("\nI can only invite 2 people for dinner. Sorry. \n")

disinvited = guest_list.pop()
print(f"I'm so sorry {disinvited}, I can't invite you cause I only space fo two") 
disinvited = guest_list.pop()
print(f"I'm so sorry {disinvited}, I can't invite you cause I only space fo two") 
disinvited = guest_list.pop()
print(f"I'm so sorry {disinvited}, I can't invite you cause I only space fo two") 
disinvited = guest_list.pop()
print(f"I'm so sorry {disinvited}, I can't invite you cause I only space fo two")

print(f"\n{guest_list[0]}, you are still invited")
print(f"{guest_list[1]}, you are still invited")

del guest_list[1]#empezamos de arriba hacia abajo
del guest_list[0]

print(guest_list)