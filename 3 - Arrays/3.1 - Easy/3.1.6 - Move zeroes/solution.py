# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example
# move_zeroes([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
# move_zeroes([0]) -> [0]

# Time complexity: O(n)
# Space complexity: O(1)

# How does it work?
# We start with an index at the beginning of the array.
# We iterate over the array.
# If the current element is not 0, we swap it with the element at the index.
# We increment the index.
# The index will be pointing to the next index where we will store the next non-zero element.
# We continue iterating.

def move_zeroes(nums: list[int]) -> None:
    index = 0

    for i in range(len(nums)):
        if nums[i]:
            if index < i:
                nums[index], nums[i] = nums[i], nums[index]
                
            index += 1