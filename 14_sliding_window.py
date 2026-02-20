# File: 14_sliding_window.py
# Topic: Sliding Window (Dynamic Size)
# Logic: We use two pointers (Left=Buy, Right=Sell). 
#        If we find a price lower than our Buy price, we slide the window to the new low.

def max_profit(prices):
    # 1. Initialize Pointers
    # Left = Buy Day (Start at index 0)
    # Right = Sell Day (Start at index 1)
    l, r = 0, 1
    
    max_p = 0 # Max Profit found so far
    
    print(f"Analyzing prices: {prices}")
    
    # 2. The Window Slide
    while r < len(prices):
        
        # Case A: Profitable Transaction? (Price[r] > Price[l])
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
            print(f"Day {l} vs Day {r}: Profit {profit}. (Max is now {max_p})")
            
        # Case B: Found a lower price? (Price[r] < Price[l])
        # If today's price is lower than our buy price, we should have bought TODAY.
        # So, snap the Left pointer to the Right pointer's location.
        else:
            print(f"Found a lower price at Day {r} ({prices[r]}). Moving Buy pointer.")
            l = r
            
        # Always move the Right pointer forward to check the next day
        r += 1
        
    return max_p

# --- Test Zone ---
stock_prices = [7, 1, 5, 3, 6, 4]
result = max_profit(stock_prices)
print(f"Maximum Profit: {result}")