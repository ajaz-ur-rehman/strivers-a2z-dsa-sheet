# Write a function that takes an array of integers and sort the array in ascending order using the selection sort algorithm.

# Example
# selection_sort([64, 25, 12, 22, 11], 5) -> [11, 12, 22, 25, 64]

# Time complexity: O(n^2)
# Space complexity: O(1)

# How does it work?
# First, we will select the range of the unsorted array using a loop (say i) that indicates the starting index of the range.
# The loop will run forward from 0 to n-1. The value i = 0 means the range is from 0 to n-1, and similarly, i = 1 means the range is from 1 to n-1, and so on.
# (Initially, the range will be the whole array starting from the first index.)
# Now, in each iteration, we will select the minimum element from the range of the unsorted array using an inner loop.
# After that, we will swap the minimum element with the first element of the selected range(in step 1). 
# Finally, after each iteration, we will find that the array is sorted up to the first index of the range. 

def selection_sort(arr: list[int], n: int):
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            
        arr[i], arr[min_idx] = arr[min_idx], arr[i]