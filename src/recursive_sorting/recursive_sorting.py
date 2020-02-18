# TO-DO: complete the helpe function below to merge 2 sorted arrays
import math


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    merged_index = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] > arrB[j]:
            merged_arr[merged_index] = arrB[j]
            j += 1

        elif arrA[i] < arrB[j]:
            merged_arr[merged_index] = arrA[i]
            i += 1

        merged_index += 1

    merged_arr = merged_arr[:merged_index]
    if i < len(arrA):
        merged_arr.extend(arrA[i:])
    if j < len(arrB):
        merged_arr.extend(arrB[j:])

    return merged_arr


test_arr1 = [2, 9, 16, 8, 18, 14, 6, 11]
test_arr2 = [1, 3, 5, 7, 9, 10]


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    mid_index = math.floor(len(arr)/2)
    left_arr = arr[:mid_index]
    right_arr = arr[mid_index:]

    left_arr_sorted = merge_sort(left_arr)
    right_arr_sorted = merge_sort(right_arr)

    return merge(left_arr_sorted, right_arr_sorted)


print(merge_sort(test_arr1))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
