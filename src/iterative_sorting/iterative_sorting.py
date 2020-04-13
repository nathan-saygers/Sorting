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

# print(selection_sort([4, 5, 1, 8, 2, 7]))


#                    cur
#                    sm

# temp = cur


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # start a swap_count variable = to 0
    swap_count = 0
    # LOOP over the array - range: 0, len(arr) - 1
    for i in range(0, len(arr) - 1):
    # Declare a left and right variable
    # start left_index = to i and right_index = to i + 1
        left = i
        right = left + 1
        print('left and right', left, right)
        print('the array', arr)
    # if left is greater than right... 
        if arr[left] > arr[right]:
            # SWAP the values at the two indexes
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    # swap_count ++
            swap_count = swap_count + 1
            print('swap count', swap_count)
    # if swap_count is greater than 0 call the bubble_sort function again
    if swap_count > 0:
        print('recur!')
        bubble_sort(arr)
    # else return the arr
    return arr

# print('here we go...', bubble_sort([4, 1, 5, 2, 7, 8]))

    # [4, 1, 5, 2, 7, 8]
#    i                          < -- first loop
#   lef          < -- second loop
#   rit / j     < -- second loop

# first loop range: i to arr length - 1
# second loop range: j to arr length - 1





# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr