# Write a function that takes in an array of integers and sorts it using Bubble Sort algorithm recursively.

# Example
# bubble_sort([64, 25, 12, 22, 11]) -> [11, 12, 22, 25, 64]

# Time complexity: O(n^2)
# Space complexity: O(n)

# How does it work?
# Bubble Sort works by repeatedly swapping the adjacent elements if they are in the wrong order.
# First, we iterate over the array using the outer loop until n - 1.
# Then, we iterate over the array using the inner loop until n - i - 1.
# If the current element is greater than the next element, we swap them.
# After each iteration of the outer loop, the largest element will be placed at the end of the array.
# We repeat the process until the array is sorted.

# Note: This is a stable sorting algorithm, meaning that the relative order of equal elements is preserved.

def bubble_sort(arr: list[int], start: int = 0) -> None:
    n = len(arr)
    
    if start >= n - 1:
        return
    
    swapped = False
    
    for i in range(n - start - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
            
    if swapped:
        bubble_sort(arr, start + 1)
        