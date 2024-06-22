# Write a function that takes an array of integers and sorts it using the quick sort algorithm.

# Example
# quick_sort([64, 25, 12, 22, 11]) -> [11, 12, 22, 25, 64]

# Time complexity: O(n log n)
# Best Case: O(n log n)
# Space complexity: O(log n)

# How does it work?
# Quick Sort works by selecting a pivot element from the array.
# We partition the array such that all elements less than the pivot are on the left and greater on the right.
# We recursively sort the two halves.
# We repeat the process until the array is sorted.

def quick_sort(arr: list[int]) -> None:
    n = len(arr)
    
    def divide(low: int, high: int) -> None:
        if low >= high:
            return
        
        pIndex = partition(low, high)
        divide(low, pIndex - 1)
        divide(pIndex + 1, high)
        
    def partition(low: int, high: int) -> None:
        pivot = arr[low]
        l, r = low, high
        
        while l < r:
            while arr[l] <= pivot and l < high:
                l += 1
                
            while arr[r] > pivot and r > low:
                r -= 1
                
            if l < r:    
                arr[l], arr[r] = arr[r], arr[l]
            
        arr[low], arr[r] = arr[r], arr[low]
        
        return r
    
    divide(0, n - 1)
