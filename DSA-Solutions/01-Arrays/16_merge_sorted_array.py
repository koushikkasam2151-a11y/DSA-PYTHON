# File: 16_merge_sorted_array.py
# Topic: Two Pointers (Backwards Strategy)
# Logic: Fill from the back to avoid overwriting data.

def merge(nums1, m, nums2, n):
    # m = count of real numbers in nums1
    # n = count of numbers in nums2
    
    # 1. Initialize Pointers at the END
    p1 = m - 1        # Last real element in nums1
    p2 = n - 1        # Last element in nums2
    p = m + n - 1     # The absolute last slot in nums1
    
    print(f"Start: nums1={nums1}, nums2={nums2}")
    
    # 2. Compare and Fill backwards
    # While both arrays still have numbers to check...
    while p1 >= 0 and p2 >= 0:
        
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
            
        p -= 1 # Move the "write" pointer back
        
    # 3. Cleanup (The Edge Case)
    # If p2 still has numbers left (but p1 is done), dump them in.
    # (We don't need to check p1, because they are already in place!)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
        
    return nums1

# --- Test Zone ---
n1 = [1, 2, 3, 0, 0, 0]
m_val = 3
n2 = [2, 5, 6]
n_val = 3

merge(n1, m_val, n2, n_val)
print(f"Merged: {n1}")