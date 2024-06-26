# Write a function that returns the second largest element in an array of integers.

# Example
# second_largest([10, 5, 10]) -> 5
# second_largest([12, 35, 1, 10, 34, 1]) -> 34
# second_largest([64, 25, 12, 22, 11], 5) -> 25

# Time complexity: O(n)
# Space complexity: O(1)

# How does it work?
# We iterate over the array and store the first and second largest elements in variables.
# We return the second largest element.

def second_largest(arr: list[int], n: int) -> int:
    first, second = -1, -1
    
    for n in arr:
        if n > first:
            second = first
            first = n
        elif n != first and n > second:
            second = n
    
    return second