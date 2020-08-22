def show_messages(messages):
    """Display messages."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Send messages"""
    while messages:
        sent_message = messages.pop()
        print(f"Sent message: {sent_message}")
        sent_messages.append(sent_message)

messages = ['hiya!', 'what\'s up', 'how\'s it going?']
sent_messages = []

print(messages)
print(sent_messages)

show_messages(messages)
send_messages(messages[:],sent_messages)

print(messages)
print(sent_messages)
