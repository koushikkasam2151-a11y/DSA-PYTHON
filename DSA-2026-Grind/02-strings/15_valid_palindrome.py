# File: 15_valid_palindrome.py
# Topic: Two Pointers & Data Cleaning
# Logic: Check if a string is a palindrome while IGNORING spaces and symbols.
#        "A man, a plan, a canal: Panama" -> "amanaplanacanalpanama" (True)

def is_palindrome(s):
    # 1. Initialize Pointers
    l = 0
    r = len(s) - 1
    
    print(f"Original: '{s}'")
    
    while l < r:
        
        # Step 2: Skip bad characters from the Left
        # isalnum() checks if it's a Letter (A-Z) or Number (0-9)
        while l < r and not s[l].isalnum():
            l += 1
            
        # Step 3: Skip bad characters from the Right
        while l < r and not s[r].isalnum():
            r -= 1
            
        # Step 4: The Comparison (Case Insensitive)
        # We use .lower() to make 'A' match 'a'
        if s[l].lower() != s[r].lower():
            print(f"Mismatch found: '{s[l]}' vs '{s[r]}'")
            return False
        
        # Step 5: Move inward
        l += 1
        r -= 1
        
    return True

# --- Test Zone ---
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"

print(f"Test 1: {is_palindrome(s1)}") # Should be True
print("-" * 20)
print(f"Test 2: {is_palindrome(s2)}") # Should be False