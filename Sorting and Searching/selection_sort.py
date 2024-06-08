def selection_sort(array):
    for i in range(0,len(array)-1):
        cur_min_index=i
        for j in range(i+1,len(array)):
            if array[j] < array[cur_min_index]:
                cur_min_index=j
        array[i],array[cur_min_index] = array[cur_min_index], array[i]
array=[10,4,7,9,3,6,1,8,2,5,3]
selection_sort(array)
print(array)