import math

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # create new array with length equal to arrA.len + arrB.len
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    #LOOP over merged array

    for i in range(0, len(merged_arr)):
        #ENSURE that arrA has not been depleted
        if len(arrA) > 0 and len(arrB) > 0:
        #COMPARE the first indexes of input arrays
            if arrA[0] > arrB[0]:
                #REPLACE the current index of merged array with the smaller element
                #REMOVE the smaller element from its parent array
                merged_arr[i] = arrB.pop(0)
            else:    
                #REPLACE the current index of merged array with the smaller element
                #REMOVE the smaller element from its parent array
                merged_arr[i] = arrA.pop(0)
        # IF arraA has been depeleted, add the remaining values of arrB
        elif len(arrA) < 1:
            #REPLACE the current index of merged array with the smaller element
            #REMOVE the smaller element from its parent array
            merged_arr[i] = arrB.pop(0)
        # IF arrB has been depeleted, add the remaining values of arrA
        else:
            #REPLACE the current index of merged array with the smaller element
            #REMOVE the smaller element from its parent array
            merged_arr[i] = arrA.pop(0)
    
    return merged_arr

# testArr = [1,2,3,4,5,6]
# print(testArr[1:])
# print(testArr[0])

# merge([1,2,3], [4,5,6])
# merge([], [])
# print(merge([6,7,8,9], [0,1,2,3,4,5]))




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #DIVIDE the input arr into a left and right half
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    #CHECK to see if the array lengths are 1
    if len(left) > 1:
        #IF NOT call merge_sort again to split arrays in half
        left = merge_sort(left)
    if len(right) > 1:
        #IF NOT call merge_sort again to split arrays in half
        right = merge_sort(right)
    
    #IF SO call return merge helper to join them together
    sorted_arr = merge(left, right)
    return sorted_arr

print(merge_sort([1, 5, 4, 8, 2, 9, 6, 0, 3, 7]))

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
