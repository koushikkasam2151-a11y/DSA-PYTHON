# File: sorting/bubble_sort.py
# Problem: Bubble Sort Implementation
# Strategy: Compare adjacent elements and swap if wrong order. O(n^2) time.

def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop: controls how many "sweeps" we do through the list
    for i in range(n):
        # Optimization flag: if we do a full sweep and swap nothing, it's sorted!
        swapped = False
        
        # Inner loop: does the actual comparing and swapping
        # We use (n - i - 1) because after every sweep, the biggest number 
        # is already locked in at the very end.
        for j in range(0, n - i - 1):
            
            # If the current number is bigger than the next one...
            if arr[j] > arr[j + 1]:
                # SWAP THEM
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If we went through the inner loop and didn't swap anything, stop early.
        if not swapped:
            break
            
    return arr

# --- Test Zone ---
unsorted_list_1 = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: [64, 34, 25, 12, 22, 11, 90]")
print(f"Sorted:   {bubble_sort(unsorted_list_1)}\n")

unsorted_list_2 = [5, 1, 4, 2, 8]
print(f"Original: [5, 1, 4, 2, 8]")
print(f"Sorted:   {bubble_sort(unsorted_list_2)}")