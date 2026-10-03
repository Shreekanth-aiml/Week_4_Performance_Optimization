import time
from original_app import find_duplicates as original_find
from optimized_app import find_duplicates as optimized_find

numbers = list(range(1000)) * 2

# Original version
start_time = time.time()
original_find(numbers)
original_time = time.time() - start_time

# Optimized version
start_time = time.time()
optimized_find(numbers)
optimized_time = time.time() - start_time

print("Original execution time:", original_time, "seconds")
print("Optimized execution time:", optimized_time, "seconds")

improvement = ((original_time - optimized_time) / original_time) * 100

print("Performance improvement:", improvement, "%")