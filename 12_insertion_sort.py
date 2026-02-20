# File: 12_insertion_sort.py
# Topic: Insertion Sort (The "Card Player" Sort)
# Logic: Take the current element and slide it backwards into the correct spot.

def insertion_sort(nums):
    n = len(nums)
    print(f"Original: {nums}")
    
    # Start from the second element (Index 1)
    # We assume the first element (Index 0) is already "sorted"
    for i in range(1, n):
        
        key = nums[i]  # The card we are holding
        j = i - 1      # The index of the card to the left
        
        # Move elements of nums[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j] # Shift the big guy to the right
            j = j - 1             # Move pointer to the left
            
        # Place the key at after the element just smaller than it.
        nums[j + 1] = key
        
        print(f"Pass {i} (Inserted {key}): {nums}")
        
    return nums

# --- Test Zone ---
data = [12, 11, 13, 5, 6]
result = insertion_sort(data)
print(f"Result:   {result}")