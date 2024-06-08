# Creating albums with Album objects
class Album:

    # This function initializes the attributes to the Album object.
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"
    
    def __eq__(self, other):  # Add equality method to allow comparison in list.index
        if isinstance(other, Album):
            return (self.album_name, self.number_of_songs, self.album_artist) == (other.album_name, other.number_of_songs, other.album_artist)
        return False


def main():
    """
        This function creates the empty list named albums1 and add elements in which each element consist
        of all the attributes of the Album class. It prints out all the elements before being sorted and 
        then sort them alphabetically followed by printing sorted list albums1.
        The function also creates the empty list named albums2 and add elements in which each element consist
        of all the attributes of the Album class. It prints out all the elements before being sorted.
        It also adds two elements to albums2 and print all elements of albums2.
        It extend(append) all the the elements of albums1 to albums2 and then sort them alphabetically followed by printing sorted list albums1.
    """
    albums1 = []
    albums1.append(Album("Thriller", 9, "Michael Jackson"))
    albums1.append(Album("Back in Black", 10, "AC/DC"))
    albums1.append(Album("The Dark Side of the Moon", 10, "Pink Floyd"))
    albums1.append(Album("Rumours", 11, "Fleetwood Mac"))
    albums1.append(Album("Born to Run", 8, "Bruce Springsteen"))

    # Print albums before sorting
    print("Albums before sorting:")
    for album in albums1:
        print(album)

    # Sort albums by number of songs
    albums1.sort(key=lambda album: album.number_of_songs)

    # Print albums after sorting
    print("\nAlbums after sorting by number of songs:")
    for album in albums1:
        print(album)

    # Swap elements at positions 1 and 2
    albums1[1], albums1[2] = albums1[2], albums1[1]

    # Print albums after swapping
    print("\nAlbums after swapping positions 1 and 2:")
    for album in albums1:
        print(album)

    albums2 = []
    albums2.append(Album("Purple Rain", 9, "Prince"))
    albums2.append(Album("Like a Prayer", 9, "Madonna"))
    albums2.append(Album("Bridge Over Troubled Water", 11, "Simon & Garfunkel"))
    albums2.append(Album("Achtung Baby", 11, "U2"))
    albums2.append(Album("Nevermind", 14, "Nirvana"))

    # Print albums2
    print("\nAlbums2:")
    for album in albums2:
        print(album)

    # Copy all albums from albums1 to albums2
    albums2.extend(albums1)

    # Add additional albums
    albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
    albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

    # Print albums2 after additions
    print("\nAlbums2 after additions:")
    for album in albums2:
        print(album)

    # Sort albums2 alphabetically by album name
    albums2.sort(key=lambda album: album.album_name)

    # Print albums2 after sorting alphabetically
    print("\nAlbums2 after sorting alphabetically:")
    for album in albums2:
        print(album)

    # Search for Dark Side of the Moon
    dark_side_index = albums2.index(Album("Dark Side of the Moon", 9, "Pink Floyd"))
    print(f"\nIndex of Dark Side of the Moon: {dark_side_index}")


if __name__ == "__main__":
    main()
