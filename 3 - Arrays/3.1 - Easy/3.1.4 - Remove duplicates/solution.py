# Write a function that removes duplicates from a sorted array of integers and returns the length of the new array.

# Example
# remove_duplicates([1, 1, 2]) -> 2
# remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4] -> 5

# Time complexity: O(n)
# Space complexity: O(1)

# How does it work?
# We create a variable to store the index representing the next index where we will store a unique element.
# We iterate over the array and compare the current element with the previous element.
# If the current element is different, we store it in the next index.
# We return the index as the length of the new array since it'll be pointing to the next index which is the length of the new array.

def remove_duplicates(nums: list[int]) -> int:
    index = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1

    return index