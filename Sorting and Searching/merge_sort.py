"""  This program defines two functions merge and merge_sort.
    It sorts the data or the elements of lists by the length of the string of each in each element of the list.
    The element with most string characters, it placed at the first position of the list and that of smallest string 
    characters is placed at the end of the list  """

def merge(left, right):
    # Merges two sorted lists (by string length) into a single sorted list.
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if len(left[i]) >= len(right[j]):
            merged.append(left[i])
            i += 1
        else:
           merged.append(right[j])
           j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

def merge_sort(data):
    """
        This function sorts a list of strings by string length (longest to shortest) using the merge sort algorithm. 
        It recursively divides the list into halves, sorts them, and then merges them back together in sorted order.
    """
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

# Sample string lists (not sorted, length >= 10)
list1 = ["hello", "world", "this", "is", "a", "longer", "sentence", "to", "test", "the", "sort"]
list2 = ["apple", "banana", "cherry", "dragonfruit", "elderberry", "fig", "grape", "honeydew", "icefruit", "jackfruit"]
list3 = ["programming", "is", "fun", "and", "challenging", "but", "rewarding", "especially", "when", "you", "solve", "a", "difficult", "problem"]

# Sort and print the lists
print("Sorted List 1:", merge_sort(list1.copy()))
print("Sorted List 2:", merge_sort(list2.copy()))
print("Sorted List 3:", merge_sort(list3.copy()))
