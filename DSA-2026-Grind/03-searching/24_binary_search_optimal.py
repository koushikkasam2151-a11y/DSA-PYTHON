def binary_search(sorted_array, target):
    left_pointer = 0
    right_pointer = len(sorted_array) - 1

    while left_pointer <= right_pointer:
        # Find the middle index
        mid_pointer = (left_pointer + right_pointer) // 2
        mid_value = sorted_array[mid_pointer]

        # Check if we found the target
        if mid_value == target:
            return mid_pointer  # Target found, return its index
        
        # If target is greater, ignore the left half
        elif mid_value < target:
            left_pointer = mid_pointer + 1
            
        # If target is smaller, ignore the right half
        else:
            right_pointer = mid_pointer - 1

    return -1  # Target not found in the array

# --- Testing the Engine ---
# The array MUST be sorted for Binary Search to work
test_array = [2, 14, 25, 33, 47, 51, 68, 89, 102]
target_number = 68

result = binary_search(test_array, target_number)

if result != -1:
    print(f"Success! Target {target_number} found at index: {result}")
else:
    print("Target not found.")