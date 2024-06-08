def quick_sort(arr,left,right):
    if left<right:
        partition_pos=partition(arr, left, right)
        quick_sort(arr,left, partition_pos-1)
        quick_sort(arr,partition_pos+1, right)

def partition(arr, left, right):
    i=left
    j=right-1
    pivot=arr[right]
    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i
arr=[3,8,4,1,7,2,14,5,11,6,9]
quick_sort(arr,0,len(arr)-1)
print(arr)