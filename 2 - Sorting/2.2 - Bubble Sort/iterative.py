# Write a function that takes in an array of integers and sorts it using Bubble Sort algorithm.

# Example
# bubble_sort([64, 25, 12, 22, 11]) -> [11, 12, 22, 25, 64]

# Time complexity: O(n^2)
# Space complexity: O(1)

# How does it work?
# Bubble Sort works by repeatedly swapping the adjacent elements if they are in the wrong order.
# First, we iterate over the array using the outer loop until n - 1.
# Then, we iterate over the array using the inner loop until n - i - 1.
# If the current element is greater than the next element, we swap them.
# After each iteration of the outer loop, the largest element will be placed at the end of the array.
# We repeat the process until the array is sorted.

def bubble_sort(arr: list[int]) -> None:
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            break