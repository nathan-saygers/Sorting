# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
# LOOP over the array
    for i in range(0, len(arr) - 1):
# save the current index for comparison to smallest index
        current_index = i
# set smallest index equal to current index
        smallest_index = current_index
    # LOOP again starting at current index
        for x in range(current_index, len(arr)):
            # IF subject of second loop is less than smallest set smallest to subject
            if arr[x] < arr[smallest_index]:
                smallest_index = x
# SWAP the value of arr[smallest] with arr[current index]
        temp = arr[current_index]
        arr[current_index] = arr[smallest_index]
        arr[smallest_index] = temp
        print('array after swap:', arr)
        
    return arr

print(selection_sort([4, 5, 1, 8, 2, 7]))


#                    cur
#                    sm

# temp = cur


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr