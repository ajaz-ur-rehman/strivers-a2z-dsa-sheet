# Write a function that takes an array of integers and sort the array in ascending order using the selection sort algorithm.

# Example
# selection_sort([64, 25, 12, 22, 11]) -> [11, 12, 22, 25, 64]

# Time complexity: O(n^2)
# Space complexity: O(1)

# How does it work?
# In Selection Sort, the array is divided into two parts: the sorted part and the unsorted part.
# Initially, the sorted part is empty and the unsorted part is the entire array.
# The smallest element from the unsorted part is selected and swapped with the first element of the unsorted part.
# This process is repeated until the entire array is sorted.

# Note: This algorithm is unstable, meaning that the relative order of equal elements is not preserved.

def selection_sort(arr: list[int]) -> None:
    n = len(arr)
    
    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    