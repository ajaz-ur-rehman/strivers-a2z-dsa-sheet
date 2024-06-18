# Given an array arr[] of n positive integers which can contain integers from 1 to p where elements can be repeated or can be absent from the array.
# Your task is to count the frequency of all numbers from 1 to n. Do modify the array in-place changes in arr[], such that arr[i] = frequency(i) and assume 1-based indexing.
# Note: The elements greater than n in the array can be ignored for counting.

# Example:
# arr[] = {2, 3, 2, 3, 5}
# n = 5
# Output:
# 0 2 2 0 1

# Time complexity: O(n)
# Space complexity: O(1)

# How does it work?
# First, we iterate over the array and set all elements greater than n to 0.
# Then, we iterate over the array and increment the element at the index of the element modulo n + 1 by n + 1 to encode the frequency.
# Finally, we iterate over the array and divide each element by n + 1 to decode the frequency.

def frequency_count(arr: list[int], n: int) -> None:
    for i in range(n):
        if arr[i] > n:
            arr[i] = 0
            
    for i in range(n):
        if arr[i] % (n + 1) > 0:
            arr[arr[i] % (n + 1) - 1] += (n + 1)
            
    for i in range(n):
        arr[i] //= (n + 1)