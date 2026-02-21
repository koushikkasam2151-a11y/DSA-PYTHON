# File: 17_majority_element.py
# Topic: Boyer-Moore Voting Algorithm
# Logic: Find the majority element (> n/2) using a "Tug of War" strategy.
#        Time: O(n), Space: O(1) - The most optimized solution possible.

def majority_element(nums):
    print(f"Voting on list: {nums}")
    
    count = 0
    candidate = None
    
    for num in nums:
        # 1. If count is 0, pick a new Candidate
        if count == 0:
            candidate = num
            print(f"  -> Count hit 0. New Candidate is: {candidate}")
        
        # 2. Vote Logic
        if num == candidate:
            count += 1
        else:
            count -= 1
            
    # The problem guarantees a majority element exists, so 'candidate' is the winner.
    return candidate

# --- Test Zone ---
test_1 = [3, 2, 3]
test_2 = [2, 2, 1, 1, 1, 2, 2]

print(f"Winner 1: {majority_element(test_1)}")
print("-" * 30)
print(f"Winner 2: {majority_element(test_2)}")