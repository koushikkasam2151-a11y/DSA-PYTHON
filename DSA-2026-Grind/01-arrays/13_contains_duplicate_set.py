# File: 13_contains_duplicate_set.py
# Topic: Using a Hash Set for O(n) speed
# Logic: Keep a history of what we've seen. If we see it again, boom.

def contains_duplicate_optimized(nums):
    # 1. Create an empty Set (The Bouncer's List)
    # Sets are faster than lists for checking "in"
    seen = set()
    
    print(f"Scanning list: {nums}")
    
    for num in nums:
        # 2. Check if we've seen this number before
        if num in seen:
            print(f"Found Duplicate: {num}")
            return True
        
        # 3. Add to the list
        seen.add(num)
        
    print("No duplicates found.")
    return False

# --- Test Zone ---
data1 = [1, 2, 3, 1]
data2 = [1, 2, 3, 4]

print("--- Test 1 ---")
contains_duplicate_optimized(data1)

print("\n--- Test 2 ---")
contains_duplicate_optimized(data2)