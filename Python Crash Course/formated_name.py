def get_formatted_name(firstname, lastname):
    """Return a full name, neatly formatted"""
    fullname = firstname + " " + lastname
    return fullname.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
