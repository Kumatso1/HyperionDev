print("linear_search is a good choice for unsorted lists as it iterates through each element") 
print("and checks for a match.It performs a linear search on the data list to find the target value.")
    
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
