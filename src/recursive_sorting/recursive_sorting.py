import math 

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    a = 0 
    b = 0

    for i in range(elements):
        if a == len(arrA):
            merged_arr[i:] = arrB[b:]
            break
        if b == len(arrB):
            merged_arr[i:] = arrA[a:]
            break
        if arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else: 
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr

print(merge([2, 3, 4, 6, 8, 8], [3, 7, 9]))

# TO-DO: implement the Merge Sort function below USING RECURSION
# TO-DO

def merge_sort( arr ):

    length = len(arr)                      

    if length == 1 or length == 0:          
        return arr                          

    breakIndex = math.floor(length/2)

    leftArray = arr[:breakIndex]
    rightArray = arr[breakIndex:]

    leftArray = merge_sort(leftArray)
    rightArray = merge_sort(rightArray)

    return merge(leftArray, rightArray)    

print(merge_sort([2, 3, 4, 6, 8, 8, 2, 3, 3, 7, 9]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
