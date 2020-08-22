def make_album(artist_name, album_title, number_of_songs=None):
    """Build a dictionary for artists and albums"""
    if number_of_songs:
        music = {'artist': artist_name, 'title': album_title,
                'songs': number_of_songs}
    else:
        music = {'artist': artist_name, 'title': album_title}
    return music

album_1 = make_album('slipknot', 'iowa')
album_2 = make_album('korn', 'life is peachy')
album_3 = make_album('disturbed', 'down with the sickness')

print(album_1)
print(album_2)
print(album_3)

album_4 = make_album('spineshank', 'self-destructive pattern', 12)
print(album_4)

while True:
    print("\nPlease enter an artist and an album.")
    print("You can quit any time by entering 'q'.\n")

    user_artist = input("Which artist?\n:")
    if user_artist == 'q':
        break

    user_title = input("Which album?\n:")
    if user_title == 'q':
        break

    user_album = make_album(user_artist, user_title)
    print(user_album)
