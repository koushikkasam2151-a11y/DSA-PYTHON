# File: 04_linear_search.py
# Date: Jan 2026
# Topic: Searching for a target (Linear Time O(n))

def linear_search(nums, target):
    """
    Scans the list from start to finish.
    Returns the INDEX if found, or -1 if not found.
    """
    print(f"Searching for: {target} in {nums}")
    
    # 1. The Scan Loop
    for i in range(len(nums)):
        
        # 2. The Check
        if nums[i] == target:
            print(f"Found it at Index: {i}")
            return i  # Return the index immediately
            
    # 3. The 'Not Found' Scenario
    # If the loop finishes without returning, the number isn't there.
    print("Target not found.")
    return -1

# --- Test Zone ---
my_data = [10, 50, 30, 70, 80, 20]
t1 = 30  # Should be Index 2
t2 = 99  # Should be -1

print("--- Test 1 ---")
linear_search(my_data, t1)

print("\n--- Test 2 ---")
linear_search(my_data, t2)