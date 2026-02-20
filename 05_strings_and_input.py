# File: 05_strings_and_input.py
# Date: Jan 2026
# Topic: User Input and Basic String Manipulation

print("--- The Name Analyzer ---")

# 1. Taking Input (Always comes as a String)
# We use input() to pause the program and wait for the user.
full_name = input("Enter your full name: ")

# 2. String Traversal (Treating text like a list)
print("\nScanning your name character by character:")
vowel_count = 0

for char in full_name:
    # Check if the character is a vowel (lower case check)
    if char.lower() in "aeiou":
        print(f"Found vowel: {char}")
        vowel_count = vowel_count + 1

# 3. Results
print(f"\nTotal length of name: {len(full_name)}")
print(f"Total vowels found: {vowel_count}")

# 4. Manual String Reversal (Bonus Logic)
reversed_name = ""
for char in full_name:
    reversed_name = char + reversed_name # Pre-pending adds it to the front!

print(f"Your name backwards is: {reversed_name}")