# Given an array arr[] sorted in ascending order of size N and an integer K. Check if K is present in the array or not.

# Example
# linear_search([1, 2, 3, 4, 5], 4) -> 1
# linear_search([1, 2, 3, 4, 5], 6) -> -1

# Time complexity: O(log n)
# Space complexity: O(1)

# How does it work?
# We start with two pointers, start and end, pointing to the beginning and end of the array.
# We calculate the mid index.
# If the mid element is greater than K, we move the end pointer to mid - 1.
# If the mid element is smaller than K, we move the start pointer to mid + 1.
# If the mid element is equal to K, we return 1.
# If the start pointer is greater than the end pointer, we return -1.
# This is a binary search algorithm.

def linear_search(arr: list[int], K: int) -> int:
    N = len(arr)
    start, end = 0, N - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] > K:
            end = mid - 1
        elif arr[mid] < K:
            start = mid + 1
        else:
            return 1
        
    return -1