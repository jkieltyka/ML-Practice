from __future__ import division
import numpy
'''
This is an algorithm warmup with quicksort
'''

def quicksort(arr, low=0, high=None):
    if high == None:
        high = len(arr) - 1
    if low < high :
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    completed = False
    while not completed:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while right >= left and arr[right] >= pivot:
            right = right - 1
        if right < left:
            completed = True
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    temp = arr[low]
    arr[low] = arr[right]
    arr[right] = temp
    return right

if __name__ == "__main__":
    in_arr = [5,6,1,4,3,7,8,11]
    sorted_arr = quicksort(in_arr)
    print sorted_arr
