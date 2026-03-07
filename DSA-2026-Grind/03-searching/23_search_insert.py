# File: 23_search_insert.py
# Problem: LeetCode 35 - Search Insert Position
# Strategy: Binary Search O(log n). If not found, return 'left' index.

def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid  # Target found! Return the index.
        
        elif nums[mid] < target:
            left = mid + 1  # Target is in the right half
            
        else:
            right = mid - 1  # Target is in the left half
            
    # The Loop Finished without finding the target.
    # The 'left' pointer is now standing exactly where the target SHOULD be.
    return left

# --- Test Zone ---
# Case 1: Target exists (5)
print(f"Test 1 (Find 5): {search_insert([1, 3, 5, 6], 5)}")   # Expected: 2

# Case 2: Target missing, belongs at the end (7)
print(f"Test 2 (Insert 7): {search_insert([1, 3, 5, 6], 7)}") # Expected: 4

# Case 3: Target missing, belongs at start (0)
print(f"Test 3 (Insert 0): {search_insert([1, 3, 5, 6], 0)}") # Expected: 0

# Case 4: Target missing, belongs in middle (2)
print(f"Test 4 (Insert 2): {search_insert([1, 3, 5, 6], 2)}") # Expected: 1