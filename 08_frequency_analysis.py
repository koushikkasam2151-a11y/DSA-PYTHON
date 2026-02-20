# File: 08_frequency_analysis.py

def isAnagram(s, t):
    # Step 1: Immediate Length Check
    if len(s) != len(t):
        return False
    
    # Step 2: Create the Scoreboard (Dictionary)
    count = {}
    
    # Step 3: Count UP for String 's'
    for char in s:
        # If we haven't seen this letter before, start it at 0
        if char not in count:
            count[char] = 0
        # Add 1
        count[char] = count[char] + 1
        
    # Step 4: Count DOWN for String 't'
    for char in t:
        # If 't' has a letter that 's' didn't have at all, fail instantly
        if char not in count:
            return False
            
        # Subtract 1
        count[char] = count[char] - 1
        
    # Step 5: The Final Audit
    # Check if every bucket is empty (0)
    for val in count.values():
        if val != 0:
            return False
            
    return True

# --- Test Zone ---
s1 = "anagram"
t1 = "nagaram"
print(f"Test 1 ({s1}, {t1}): {isAnagram(s1, t1)}")  # Should be True

s2 = "rat"
t2 = "car"
print(f"Test 2 ({s2}, {t2}): {isAnagram(s2, t2)}")  # Should be False