favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['kevin', 'tom', 'jen', 'sarah']

for name in people:
    if name in favorite_languages.keys():
        print("Thank you " + name.title() + " for taking the poll")
    else:
        print("Hi " + name.title()  + " take our programming language poll")
