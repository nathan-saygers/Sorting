# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(i, arr[-1]):
            if j < smallest_index:
                smallest_index = j

        # TO-DO: swap
        temp = cur_index
        cur_index = smallest_index
        smallest_index = temp



    return arr
    
print(selection_sort([4, 5, 1, 8, 2, 7]))


#       cur
#        sm

# temp = cur


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr