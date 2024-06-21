# Write a function that takes an array of integers and sorts it using the merge sort algorithm.

# Example
# merge_sort([64, 25, 12, 22, 11]) -> [11, 12, 22, 25, 64]

# Time complexity: O(n log n)
# Best Case: O(n log n)
# Space complexity: O(n)

# How does it work?
# Merge Sort works by dividing the array into two halves.
# We recursively sort the two halves.
# We merge the two sorted halves.
# We repeat the process until the array is sorted.

def merge_sort(arr: list[int]) -> None:
    n = len(arr)
    
    def divide(low: int, high: int) -> None:
        if low >= high:
            return
        
        mid = (low + high) // 2
        divide(low, mid)
        divide(mid + 1, high)
        merge(low, mid, high)
        
    def merge(low: int, mid: int, high: int) -> None:
        l, r = low, mid + 1
        res = []
        
        while l <= mid and r <= high:
            if arr[l] <= arr[r]:
                res.append(arr[l])
                l += 1
            else:
                res.append(arr[r])
                r += 1
                
        while l <= mid:
            res.append(arr[l])
            l += 1
            
        while r <= high:
            res.append(arr[r])
            r += 1
            
        for i in range(len(res)):
            arr[i + low] = res[i]
    
    divide(0, n - 1)
