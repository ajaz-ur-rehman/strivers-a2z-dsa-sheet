# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.

# Example
# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].

# Time complexity: O(n log n)
# Space complexity: O(1)

# How does it work?
# First, we sort the array.
# Then, we use a sliding window to find the maximum frequency of an element.
# We initialize two pointers, l and r, to 0.
# We initialize res and total to 0.
# We iterate over the array using the right pointer.
# We add the element at the right pointer to the total.
# We iterate over the array using the left pointer.
# We remove the element at the left pointer from the total if the total exceeds the sum of the elements in the window plus k.
# We update the result with the maximum frequency.
# We increment the right pointer.
# We return the result.

def max_frequency(nums: list[int], k: int) -> int:
    nums.sort()

    l, r = 0, 0
    res, total = 0, 0

    while r < len(nums):
        total += nums[r]

        while nums[r] * (r - l + 1) > (total + k):
            total -= nums[l]
            l += 1

        res = max(res, r - l + 1)
        r += 1

    return res