# Write a function that takes an array as input and returns the array in reversed order using recursion.

# Example
# reverse_array([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
# reverse_array([1, 2, 3]) -> [3, 2, 1]
# reverse_array([]) -> []

# Time complexity: O(n)
# Space complexity: O(n)

# How does it work?
# The function returns an empty list if the input array is empty.
# Otherwise, it returns a list containing the last element of the array and the result of calling the function with the array without the last element.
# The function concatenates the two lists and returns the result.

def reverse_array(arr: list) -> list:
    if len(arr) == 0:
        return []
    
    return [arr[-1]] + reverse_array(arr[:-1])