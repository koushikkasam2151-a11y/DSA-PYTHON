# File: 09_two_sum.py
# Topic: Finding a pair that adds up to a target using a Dictionary

def twoSum(nums, target):
    # 1. The "Guest List" (Stores {value: index})
    seen = {}
    
    print(f"Target is: {target}")
    
    # 2. Walk through the party
    for i, num in enumerate(nums):
        # Calculate who we need
        needed = target - num
        
        # 3. Check the list
        if needed in seen:
            # Found the partner!
            print(f"Match Found! {num} needs {needed}")
            # Return the index of the partner (from the map) and current index
            return [seen[needed], i]
        
        # 4. If not found, add myself to the list
        seen[num] = i
        print(f"Added {num} at index {i} to the list.")
        
    return []

# --- Test Zone ---
numbers = [2, 7, 11, 15]
goal = 9

result = twoSum(numbers, goal)
print(f"Indices: {result}")