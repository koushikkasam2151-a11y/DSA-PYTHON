# File: 19_roman_to_integer.py
# Problem: LeetCode 13 - Roman to Integer
# Strategy: Hash Map lookup with a look-ahead for subtraction.

def roman_to_int(s):
    # 1. The Translation Dictionary
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    n = len(s)
    
    # 2. The Scan
    for i in range(n):
        current_val = roman_map[s[i]]
        
        # Check if we are NOT at the last character
        # AND if the current value is less than the next value
        if i < n - 1 and current_val < roman_map[s[i + 1]]:
            # It's a subtraction case (like IV or IX)
            total -= current_val
        else:
            # It's a normal addition case (like VI or CX)
            total += current_val
            
    return total

# --- Test Zone ---
print(f"Test 1 (III): {roman_to_int('III')}")       # Expected: 3
print(f"Test 2 (LVIII): {roman_to_int('LVIII')}")   # Expected: 58 (50 + 5 + 1 + 1 + 1)
print(f"Test 3 (MCMXCIV): {roman_to_int('MCMXCIV')}") # Expected: 1994