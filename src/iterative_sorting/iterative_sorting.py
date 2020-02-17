# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


test_list = [2, 5, 1, 4, 6, 3, 7, -1, 11, 9, 9]
print(selection_sort(test_list))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        # cur_index = i
        # smallest_index = cur_index
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(bubble_sort(test_list))
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
