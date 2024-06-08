# # Creating albums with Album objects
# class Album:
#     def __init__(self, album_name, number_of_songs, album_artist):
#         self.album_name = album_name
#         self.number_of_songs = number_of_songs
#         self.album_artist = album_artist

#     def __str__(self):
#         return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"
    
#     def __eq__(self, other):  # Add equality method to allow comparison in list.index
#         if isinstance(other, Album):
#             return (self.album_name, self.number_of_songs, self.album_artist) == (other.album_name, other.number_of_songs, other.album_artist)
#         return False


# def main():
#     albums1 = []
#     albums1.append(Album("Thriller", 9, "Michael Jackson"))
#     albums1.append(Album("Back in Black", 10, "AC/DC"))
#     albums1.append(Album("The Dark Side of the Moon", 10, "Pink Floyd"))
#     albums1.append(Album("Rumours", 11, "Fleetwood Mac"))
#     albums1.append(Album("Born to Run", 8, "Bruce Springsteen"))

#     # Print albums before sorting
#     print("Albums before sorting:")
#     for album in albums1:
#         print(album)

#     # Sort albums by number of songs
#     albums1.sort(key=lambda album: album.number_of_songs)

#     # Print albums after sorting
#     print("\nAlbums after sorting by number of songs:")
#     for album in albums1:
#         print(album)

#     # Swap elements at positions 1 and 2
#     albums1[1], albums1[2] = albums1[2], albums1[1]

#     # Print albums after swapping
#     print("\nAlbums after swapping positions 1 and 2:")
#     for album in albums1:
#         print(album)

#     albums2 = []
#     albums2.append(Album("Purple Rain", 9, "Prince"))
#     albums2.append(Album("Like a Prayer", 9, "Madonna"))
#     albums2.append(Album("Bridge Over Troubled Water", 11, "Simon & Garfunkel"))
#     albums2.append(Album("Achtung Baby", 11, "U2"))
#     albums2.append(Album("Nevermind", 14, "Nirvana"))

#     # Print albums2
#     print("\nAlbums2:")
#     for album in albums2:
#         print(album)

#     # Copy all albums from albums1 to albums2
#     albums2.extend(albums1)

#     # Add additional albums
#     albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
#     albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

#     # Print albums2 after additions
#     print("\nAlbums2 after additions:")
#     for album in albums2:
#         print(album)

#     # Sort albums2 alphabetically by album name
#     albums2.sort(key=lambda album: album.album_name)

#     # Print albums2 after sorting alphabetically
#     print("\nAlbums2 after sorting alphabetically:")
#     for album in albums2:
#         print(album)

#     # Search for Dark Side of the Moon
#     dark_side_index = albums2.index(Album("Dark Side of the Moon", 9, "Pink Floyd"))
#     print(f"\nIndex of Dark Side of the Moon: {dark_side_index}")


# if __name__ == "__main__":
#     main()

def linear_search(data, target):
  """
  Performs a linear search on the data list to find the target value.

  Args:
      data: The list to search.
      target: The value to search for.

  Returns:
      The index of the target value in the list if found, otherwise -1.
  """
  for i, value in enumerate(data):
    if value == target:
      return i
  return -1

def insertion_sort(data):
    """
    Sorts a list of numbers in ascending order using Insertion Sort.

    Args:
      data: The list to sort.

    Returns:
      The sorted list.
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
    while j >= 0 and key < data[j]:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key
    return data

def binary_search(data, target):
    """
    Performs a binary search on the sorted data list to find the target value.

    Args:
      data: The sorted list to search.
      target: The value to search for.

    Returns:
      The index of the target value in the list if found, otherwise -1.
    """
    low = 0
    high = len(data) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


# Sample data
data = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Linear Search (suitable for unsorted lists)
search_result = linear_search(data, 9)
if search_result != -1:
  print(f"Number 9 found at index {search_result} (using Linear Search)")
else:
  print("Number 9 not found (using Linear Search)")

# Insertion Sort
sorted_data = insertion_sort(data.copy())  # Sort a copy to avoid modifying original
print("\nSorted data:", sorted_data)

# Binary Search (efficient for sorted lists)
search_result = binary_search(sorted_data, 9)
if search_result != -1:
  print(f"\nNumber 9 found at index {search_result} (using Binary Search)")
else:
  print("Number 9 not found (using Binary Search)")

# Binary Search Usage
print("\nBinary Search is efficient for situations where the data is sorted and")
print("you need to perform frequent searches on the same data set. This is")
print("common in real-world applications like searching through large datasets")
print("or implementing algorithms like hash tables.")
