messages_1 = ["hello", "good morning", "good afternoon", "good evening", "good bye"]
sent_messages_1 = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        enviados = messages.pop()
        print(enviados)
        sent_messages.append(enviados)



print("\nShowing all messages")
show_messages(messages_1)
    


print("\nShowing sent messages")
send_messages(messages_1[:], sent_messages_1)

print(messages_1)
print(sent_messages_1)