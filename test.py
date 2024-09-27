import time

# Test on random, sorted, and reverse-sorted arrays
def time_selection_algorithm(select_func, arr, k):
    start = time.time()
    result = select_func(arr, k)
    end = time.time()
    return result, end - start

# Generating test data
sizes = [1000, 5000, 10000, 50000]
for size in sizes:
    random_array = [random.randint(0, 100000) for _ in range(size)]
    sorted_array = sorted(random_array)
    reversed_array = sorted_array[::-1]
    
    print(f"Testing size: {size}")
    
    for select_func in [deterministic_select, randomized_select]:
        for arr in [random_array, sorted_array, reversed_array]:
            _, time_taken = time_selection_algorithm(select_func, arr, size // 2)
            print(f"{select_func.__name__} on size {size}: {time_taken:.5f} seconds")
