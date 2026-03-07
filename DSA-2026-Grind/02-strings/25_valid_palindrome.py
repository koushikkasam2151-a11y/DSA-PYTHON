# File: 24_valid_palindrome.py
# Problem: LeetCode 125 - Valid Palindrome
# Strategy: Two Pointers moving inwards. Ignore non-alphanumeric characters.

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # 1. Skip garbage characters from the left
        # .isalnum() checks if it's a letter or a number
        while left < right and not s[left].isalnum():
            left += 1
        
        # 2. Skip garbage characters from the right
        while left < right and not s[right].isalnum():
            right -= 1
            
        # 3. Compare the characters (force lowercase to be safe)
        if s[left].lower() != s[right].lower():
            return False  # Mismatch found! Not a palindrome.
            
        # 4. If they match, move both pointers inward to check the next pair
        left += 1
        right -= 1
        
    # If the pointers cross and we never found a mismatch, it's valid!
    return True

# --- Test Zone ---
# Case 1: The messy classic
print(f"Test 1: {is_palindrome('A man, a plan, a canal: Panama')}") # Expected: True

# Case 2: Almost, but no
print(f"Test 2: {is_palindrome('race a car')}")                     # Expected: False

# Case 3: Empty string (technically reads the same backwards)
print(f"Test 3: {is_palindrome(' ')}")                              # Expected: True