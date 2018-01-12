current_users = ['root', 'guest', 'alex', 'ted', 'tor']
new_users = ['alex', 'tom', 'ted', 'ben', 'pal']

for user in new_users:
    if user.lower() in current_users:
        print("Hi "+user.title()+", username is already taken, please enter new username")
    else:
        print("Hi "+user.title()+", username is available")
