# File: 06_manual_stats.py
# Date: Jan 2026
# Topic: Calculating Sum and Average manually

def calculate_stats(nums):
    """
    Computes total and average without using sum() or len() logic shortcuts.
    """
    total_sum = 0
    count = 0
    
    # 1. The Accumulator Loop
    for num in nums:
        total_sum = total_sum + num  # Add current number to the pile
        count = count + 1            # Count how many numbers we have seen
        
    # 2. Calculate Average (Prevent division by zero)
    if count == 0:
        average = 0
    else:
        average = total_sum / count
        
    return total_sum, average

# --- Test Zone ---
expenses = [500, 200, 440, 118, 300] # Your Jan Expenses
total, avg = calculate_stats(expenses)

print(f"Expenses: {expenses}")
print(f"Total Burn: ₹{total}")
print(f"Average Spend: ₹{avg}")