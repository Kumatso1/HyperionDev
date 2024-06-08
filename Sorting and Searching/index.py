class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"


    def add_and_sort_albums(albums):
        """
        This function takes a list of albums and adds user-provided albums to it.
        It then sorts the list alphabetically by album name and returns the updated list.
        """
        while True:
            album_name = input("Enter album name (blank to quit): ")
            if not album_name:
                break
            number_of_songs = int(input("Enter number of songs: "))
            album_artist = input("Enter album artist: ")
            albums.append(Album(album_name, number_of_songs, album_artist))

        albums.sort(key=lambda album: album.album_name)  # Sort by album name
        return albums


    def search_album(albums, album_name):
        """
        This function searches for an album by name in the given list and returns its index.
        If not found, it returns -1.
        """
        try:
            return albums.index(Album(album_name, None, None))  # Search by name only
        except ValueError:
            return -1


def main():
    albums = []

    # Add and sort albums using the function
    albums = add_and_sort_albums(albums)

    # Print sorted albums
    print("\nAlbums:")
    for album in albums:
        print(album)

    # Search for an album
    search_term = input("\nEnter album name to search: ")
    search_index = search_album(albums, search_term)

    for i in range(len(arr)):
        if arr[i] == item:
            return i


if __name__ == "__main__":
    main()
