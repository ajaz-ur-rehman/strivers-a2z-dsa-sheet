# Write a function that returns the largest element in a list of integers.

# Example
# largest([64, 25, 12, 22, 11], 5) -> 64

# Time complexity: O(n)
# Space complexity: O(1)

# How does it work?
# We iterate over the array and store the largest element in a variable.
# We return the largest element.

def largest(arr: list[int], n: int) -> int:
    if n == 0:
        return -1
    
    res = arr[0]
    
    for i in range(1, n):
        if arr[i] > res:
            res = arr[i]
            
    return res