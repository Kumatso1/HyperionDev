""" list2=[]
def dali_sort(list1):
    for element in range(len(list1)):
        for i in list1:
            if list1[i]==min(list1):
                temp=list1[i]
            list2.append(temp)
            list1=list1.pop(temp)
        
    return list2
list1=[5,3,4,1,2]
dali_sort(list1)
print(list2)
 
 """
def selection_sort(original_list):
   '''
    Sorts a list in ascending order using selection sort.

    Args:
        original_list (list): The list to be sorted.

    Returns:
        list: The sorted list.
    '''
   sorted_list = []
   for _ in range(len(original_list)):
        min_index = 0
        for i in range(1, len(original_list)):
            if original_list[i] < original_list[min_index]:
                min_index = i
        sorted_list.append(original_list[min_index])
        original_list.pop(min_index)  # Remove the minimum element from the original list
        print(original_list)
        print(sorted_list)
   return sorted_list

# Example usage
original_list = [5, 2, 8, 1, 9,23,3,7,4,16]
sorted_list = selection_sort(original_list.copy())  # Avoid modifying the original list
print("Original list:", original_list)
print("Sorted list:", sorted_list)
