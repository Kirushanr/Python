prompt = "\nTell me something i will repeat it"
prompt += "\nEnter 'quit' to end program : "

message = ""
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
