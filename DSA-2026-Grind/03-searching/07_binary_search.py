# File: 07_binary_search.py
# Date: Feb 1, 2026
# Topic: Binary Search (O(log n)) - The Divide and Conquer Strategy

def binary_search(nums, target):
    """
    Finds the target index by constantly cutting the search space in half.
    PRE-CONDITION: List MUST be sorted.
    """
    low = 0
    high = len(nums) - 1
    
    print(f"Searching for {target} in {nums}...")
    
    # Keep searching as long as the search space is valid
    while low <= high:
        # 1. Find the Middle Index
        # (low + high) // 2 does integer division (drops the decimal)
        mid = (low + high) // 2
        guess = nums[mid]
        
        print(f"Checking Middle Index: {mid}, Value: {guess}")
        
        # 2. The Check
        if guess == target:
            return mid  # Found it!
        
        # 3. The Adjustment
        if guess > target:
            # The guess was too HIGH.
            # So the target must be in the LEFT half.
            # Move the 'high' wall to the left of mid.
            high = mid - 1
            
        else:
            # The guess was too LOW.
            # So the target must be in the RIGHT half.
            # Move the 'low' wall to the right of mid.
            low = mid + 1
            
    return -1  # Target not found

# --- Test Zone ---
# REMEMBER: The list MUST be sorted for this to work!
my_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target_val = 80

result = binary_search(my_data, target_val)

if result != -1:
    print(f"SUCCESS: Found {target_val} at Index {result}")
else:
    print("FAILURE: Target not in list.")