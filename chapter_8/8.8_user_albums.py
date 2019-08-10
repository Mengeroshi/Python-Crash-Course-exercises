def make_album(artist_name, album_name, songs = None):
    if songs:
        album_info = {"artist" : artist_name, "album" : album_name, "song number" : songs}
    else:
        album_info = {"artist" : artist_name, "album" : album_name}
    
    return album_info

while True:
    print("Write the information about your favourite music album.")
    print("Insert q to finish")
    
    artist_name1 = input("Artist Name: ")
    if artist_name1 == "q":
        break
    album_name1 = input("Album Name: ")
    if album_name1 == "q":
        break
    song_number = input("Songs in the album (press enter if you don't remember): ")

    album_view = make_album(artist_name1, album_name1, song_number)
    print(album_view)
