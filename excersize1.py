#!usr/bin/python3
"""
    Code for sorting list for the task.
"""
def selection_sort(arr):
    """
        This sorts the first 5 elements in ascending order,
        the last 5 elements in decreasing order and reverses
        elements between them.
    """
    num = len(arr)
    for i in range(5):
        min_idx = i
        for j in range(i+1, 5):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    for i in range(num-5, num):
        max_idx = i
        for j in range(i+1, num):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    for i in range(5, num-5):
        arr[i] = arr[num-i-1]

    return arr
def main():
    """
        This is yhe main.
    """
    arr = [5,3,7,9,1,4,6,7,9,3,1,9,5,4,7]
    print(selection_sort(arr))
main()
