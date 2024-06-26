# Write a function that takes in an array of integers and returns whether the array is sorted and rotated.

# Example
# check_sorted_and_rotated([3, 4, 5, 1, 2]) -> True
# check_sorted_and_rotated([2, 1, 3, 4]) -> False
# check_sorted_and_rotated([1, 2, 3]) -> True

# Time complexity: O(n)
# Space complexity: O(1)

# How does it work?
# We iterate over the array and find the index where the array is not sorted.
# We update the index and continue iterating.
# If we find another index where the array is not sorted, we return False.
# If we find an index, we check if the first element is greater than or equal to the last element.
# If we find no index, we return True.


def check_sorted_and_rotated(nums: list[int]) -> bool:
    n = len(nums)
    index = None

    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            if index:
                return False
            
            index = i

    if index:
        return nums[0] >= nums[-1]
    
    return True