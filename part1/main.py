import random

# Deterministic Algorithm: Median of Medians (Selection in Worst-Case Linear Time)
def deterministic_select(arr, k):
    # Base case: if the array is small, sort and return the k-th smallest element
    if len(arr) <= 5:
        return sorted(arr)[k-1]
    
    # Step 1: Divide the array into sublists of length 5
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    
    # Step 2: Find the median of each sublist
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    
    # Step 3: Recursively find the median of the medians
    median_of_medians = deterministic_select(medians, len(medians)//2 + 1)
    
    # Step 4: Partition the array around the median of medians
    lows = [el for el in arr if el < median_of_medians]
    highs = [el for el in arr if el > median_of_medians]
    pivots = [el for el in arr if el == median_of_medians]
    
    # Step 5: Recur based on the partition sizes
    if k <= len(lows):
        return deterministic_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return median_of_medians
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))

# Randomized Algorithm: Randomized Quickselect (Selection in Expected Linear Time)
def randomized_select(arr, k):
    # Base case: if the array has only one element, return that element
    if len(arr) == 1:
        return arr[0]
    
    # Step 1: Choose a pivot randomly
    pivot = random.choice(arr)
    
    # Step 2: Partition the array around the pivot
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    
    # Step 3: Recur based on the partition sizes
    if k <= len(lows):
        return randomized_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))

# Test cases including duplicates
test_array_with_duplicates = [12, 3, 5, 7, 19, 26, 1, 2, 13, 15, 16, 5, 7, 12, 19, 26, 7, 7]
k = 5

# Deterministic selection
det_result_duplicates = deterministic_select(test_array_with_duplicates, k)

# Randomized selection
rand_result_duplicates = randomized_select(test_array_with_duplicates, k)

# Printing the results
print(f"Deterministic Selection Result (with duplicates): {det_result_duplicates}")
print(f"Randomized Selection Result (with duplicates): {rand_result_duplicates}")

