# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example
# rotate([1, 2, 3, 4, 5, 6, 7], 3) -> [5, 6, 7, 1, 2, 3, 4]
# rotate([-1, -100, 3, 99], 2) -> [3, 99, -1, -100]

# Time complexity: O(n)
# Space complexity: O(1)

# How does it work?
# We reverse the entire array.
# We reverse the first k elements.
# We reverse the remaining elements.

def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n

    if k == 0:
        return

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1