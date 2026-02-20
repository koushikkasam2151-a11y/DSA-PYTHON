# File: 21_valid_parentheses.py
# Problem: LeetCode 20 - Valid Parentheses
# Strategy: Stack (LIFO) and a Hash Map for matching pairs.

def is_valid(s):
    # 1. The Stack (to hold our "open" brackets)
    stack = []
    
    # 2. The Map (Keys = Closing brackets, Values = Opening brackets)
    # This helps us instantly know what we are looking for.
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # 3. Process the string one character at a time
    for char in s:
        if char in bracket_map:
            # It's a CLOSING bracket.
            # Pop the top element from the stack if it's not empty, else assign a dummy value '#'
            top_element = stack.pop() if stack else '#'
            
            # Does the popped bracket match what this closing bracket needs?
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an OPENING bracket. Push it onto the stack.
            stack.append(char)
            
    # 4. Final Check: If the stack is empty, every bracket found its partner.
    return not stack

# --- Test Zone ---
print(f"Test 1 '()': {is_valid('()')}")             # Expected: True
print(f"Test 2 '()[]{{}}': {is_valid('()[]{}')}")   # Expected: True
print(f"Test 3 '(]': {is_valid('(]')}")             # Expected: False
print(f"Test 4 '([)]': {is_valid('([)]')}")         # Expected: False
print(f"Test 5 '{{[]}}': {is_valid('{[]}')}")       # Expected: True