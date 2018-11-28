def make_album(artist, album, dor=''):
    concert = {'artist': artist, 'album': album}
    if dor:
        concert['dor'] = dor
    return concert
while True:
    print("\nEnter your favourite music:")
    a_artis = input("Artist:")
    if a_artis == 'q':
        break

    b_album = input("Album:")
    if b_album == 'q':
        break

    d_dor = input("Dorozhka:")
    if d_dor == 'q':
        break

    formatted_album = make_album(a_artis, b_album, d_dor)
    print(str(formatted_album))
