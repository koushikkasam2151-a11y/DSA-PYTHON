# File: 11_selection_sort.py
# Topic: Selection Sort (The "Sniper" Sort)
# Logic: Find the minimum element in the unsorted part and swap it to the front.

def selection_sort(nums):
    n = len(nums)
    print(f"Original: {nums}")
    
    # Outer Loop: The "Slot" we are trying to fill
    # We go from 0 to n-1
    for i in range(n):
        
        # Step 1: Assume the current slot holds the minimum
        min_index = i
        
        # Step 2: The Sniper Scope (Scan the rest of the list)
        for j in range(i + 1, n):
            # If we find someone smaller than our current minimum...
            if nums[j] < nums[min_index]:
                min_index = j  # Update the target index
                
        # Step 3: The Swap (Only happens once per pass)
        # We put the smallest number found into the current slot 'i'
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
            
        print(f"Pass {i}: {nums}") # See the list getting fixed slowly
            
    return nums

# --- Test Zone ---
data = [64, 25, 12, 22, 11]
result = selection_sort(data)
print(f"Result:   {result}")