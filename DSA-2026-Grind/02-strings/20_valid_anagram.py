# File: 20_valid_anagram.py
# Problem: LeetCode 242 - Valid Anagram
# Strategy: Frequency Counting using a Dictionary

def is_anagram(s, t):
    # 1. Fast Fail: If lengths don't match, it's impossible.
    if len(s) != len(t):
        return False
        
    # 2. The Frequency Map
    counts = {}
    
    # 3. Add for string 's', Subtract for string 't'
    for i in range(len(s)):
        # counts.get(key, 0) returns 0 if the key doesn't exist yet
        counts[s[i]] = counts.get(s[i], 0) + 1
        counts[t[i]] = counts.get(t[i], 0) - 1
        
    # 4. Verification: The map should be completely neutralized (all zeros)
    for count in counts.values():
        if count != 0:
            return False
            
    return True

# --- Test Zone ---
print(f"Test 1 (anagram, nagaram): {is_anagram('anagram', 'nagaram')}") # Expected: True
print(f"Test 2 (rat, car): {is_anagram('rat', 'car')}")                 # Expected: False