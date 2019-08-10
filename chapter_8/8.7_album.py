def make_album(artist_name, album_name, songs = None):
    if songs:
        album_info = {"artist" : artist_name, "album" : album_name, "song number" : songs}
    else:
        album_info = {"artist" : artist_name, "album" : album_name}
    
    return album_info

album_1 = make_album("kendrick lamar", "damn")
print(album_1)

album_2 = make_album("steve angello", "human", 20)
print(album_2)

album_3 = make_album("Alesso", "Forever")
print(album_3)