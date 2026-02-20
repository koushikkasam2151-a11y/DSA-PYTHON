# File: 10_bubble_sort.py
# Topic: Bubble Sort (The "Sinking Sort") - OPTIMIZED
# Logic: Push the largest element to the end in every pass.

def bubble_sort(nums):
    n = len(nums)
    print(f"Original: {nums}")
    
    # Outer Loop: Controls the "Passes"
    for i in range(n):
        
        # The 'Smart' Flag
        # Assume the list is sorted until proven otherwise
        swapped = False
        
        # Inner Loop: The "Comparator"
        # We stop at n-i-1 because the last 'i' items are already sorted!
        for j in range(0, n - i - 1):
            
            # Compare neighbor
            if nums[j] > nums[j + 1]:
                # SWAP Logic
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True  # We had to do work, so it wasn't sorted yet
        
        # Optimization Check:
        # If we went through the whole list and didn't swap ONCE, we are done.
        if not swapped:
            print(f"Stopped early at pass {i}! List is already sorted.")
            break
                
    return nums

# --- Test Zone ---
data = [1,2,3,4,5]
sorted_data = bubble_sort(data)
print(f"Sorted:   {sorted_data}")