# File: 18_best_time_stock.py
# Problem: LeetCode 121 - Best Time to Buy and Sell Stock
# Strategy: One Pass (Greedy) - Track the lowest valley and max profit.

def max_profit(prices):
    # 1. Edge Case: Empty list or just 1 day (can't sell)
    if not prices or len(prices) < 2:
        return 0
        
    # 2. Initialize Variables
    # min_price: The lowest price we've seen SO FAR (Start infinite)
    min_price = float('inf') 
    max_profit = 0
    
    # 3. The One Pass Scan
    for price in prices:
        # Case A: Is this price lower than our current lowest?
        if price < min_price:
            min_price = price # We found a new "dip" to buy at
            
        # Case B: If we sold today, would we make a record profit?
        elif (price - min_price) > max_profit:
            max_profit = price - min_price
            
    return max_profit

# --- Test Zone ---
# Case 1: Standard
print(f"Test 1: {max_profit([7, 1, 5, 3, 6, 4])}") # Expected: 5 (Buy at 1, Sell at 6)

# Case 2: Crash Market (No profit possible)
print(f"Test 2: {max_profit([7, 6, 4, 3, 1])}")    # Expected: 0