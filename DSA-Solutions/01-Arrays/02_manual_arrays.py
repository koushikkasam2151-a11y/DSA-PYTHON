# File: 02_manual_arrays.py
# Date: Jan 2026
# Topic: Finding Max, Min, and Range WITHOUT built-in functions

def get_range(nums):
    """
    Calculates the difference between the largest and smallest number.
    Strategy: Assume the first number is the champion, then challenge everyone.
    """
    
    # 1. Initialize Champions (Assume first number holds both titles)
    current_max = nums[0]
    current_min = nums[0]
    
    # 2. The Inspection Loop (Linear Scan)
    for num in nums:
        
        # Check for new Heavyweight Champion (Max)
        if num > current_max:
            current_max = num
            
        # Check for new Lightweight Champion (Min)
        if num < current_min:
            current_min = num
            
    # 3. Calculate Result (Outside the loop)
    result = current_max - current_min
    
    print(f"List: {nums}")
    print(f"Max: {current_max}")
    print(f"Min: {current_min}")
    print(f"Range: {result}")
    return result

# --- Test Zone ---
scores = [10, 5, 20, 50, 2]
get_range(scores)