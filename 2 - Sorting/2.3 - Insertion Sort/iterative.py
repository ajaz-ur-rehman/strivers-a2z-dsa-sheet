# Write a function that takes an array of integers and sorts it using the insertion sort algorithm.

# Example
# insertion_sort([64, 25, 12, 22, 11]) -> [11, 12, 22, 25, 64]

# Time complexity: O(n^2)
# Best Case: O(n) when the array is already sorted.
# Space complexity: O(1)

# How does it work?
# Insertion Sort works by iterating over the array starting from the second element.
# We store the current element in a variable key.
# We iterate over the array from the current element to the first element.
# If the current element is less than the key, we shift the elements to the right.
# We insert the key at the correct position.
# We repeat the process until the array is sorted.

# Note: This is a stable sorting algorithm, meaning that the relative order of equal elements is preserved.

def insertion_sort(arr: list[int]) -> None:
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        