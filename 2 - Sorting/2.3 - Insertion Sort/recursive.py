# Write a function that takes an array of integers and sorts it using the insertion sort algorithm recursively.

# Example
# insertion_sort([64, 25, 12, 22, 11]) -> [11, 12, 22, 25, 64]

# Time complexity: O(n^2)
# Best Case: O(n) when the array is already sorted.
# Space complexity: O(n)

# How does it work?
# Insertion Sort works by iterating over the array starting from the second element.
# We store the current element in a variable key.
# We iterate over the array from the current element to the first element.
# If the current element is less than the key, we shift the elements to the right.
# We insert the key at the correct position.
# We repeat the process until the array is sorted.

# Note: This is a stable sorting algorithm, meaning that the relative order of equal elements is preserved.

def insertion_sort(arr: list[int], start: int = 1) -> None:
    n = len(arr)
    
    if start >= n:
        return
    
    key = arr[start]
    i = start - 1
    
    while i >= 0 and key < arr[i]:
        arr[i + 1] = arr[i]
        i -= 1
        
    arr[i + 1] = key
    
    insertion_sort(arr, start + 1)
