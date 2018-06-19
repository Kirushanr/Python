def make_album(artist_name, album_title, number_of_tracks=''):
    """Return dictionary containing album information"""
    temp_album = {'artist': artist_name.title(), 'album': album_title.title()}
    # check if the user has provided no of tracks
    if number_of_tracks:
        temp_album['number_of_tracks'] = number_of_tracks

    return temp_album


Flag = True
while Flag:
    album = input('Enter the title of the album: ')
    artist = input('Enter the name of the aritst: ')
    record = make_album(album, artist)
    print(record)
    prompt = input("\nType 'yes' to quit, 'no' to continue entering: ")

    if prompt == 'yes':
        Flag = False  # set the flag to False, as the user wants to quit
