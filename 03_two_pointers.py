# File: 03_two_pointers.py
# Date: Jan 2026
# Topic: Reversing a List In-Place (Two Pointer Strategy)

def reverse_list_manual(nums):
    """
    Reverses a list by swapping the first and last elements,
    then moving inward until the pointers meet.
    """
    print(f"Original: {nums}")
    
    # 1. Initialize Pointers
    left = 0                # Start index
    right = len(nums) - 1   # End index (Length - 1)
    
    # 2. The 'Walking' Loop
    # Keep going as long as Left is strictly smaller than Right
    while left < right:
        
        # 3. The Swap Logic
        # (We swap the values at the left and right indices)
        nums[left], nums[right] = nums[right], nums[left]
        
        # 4. Move Pointers Inward
        left = left + 1     # Move forward
        right = right - 1   # Move backward
        
    return nums

# --- Test Zone ---
my_data = [1, 2, 3, 4, 5]
result = reverse_list_manual(my_data)
print(f"Reversed: {result}")