prompt = "\nTell me something and I'll repeat it back to you."
prompt += "\nEnter 'quit' to end the program.\n:"

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"\n{message}")
