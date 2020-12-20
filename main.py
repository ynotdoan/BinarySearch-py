
import time, random
from binary_search import BinarySearch as BS


nums = []
# appends number in range to list nums
for i in range(0, 1_000_000):
  nums.append(i) 
  
# start timer
start = time.perf_counter()

res = BS(nums, 1001)
print (res.b_search())

# subtracts current time with start time to get time ran
# multiply by 1000 to return time in ms.
time_diff = (time.perf_counter() - start) * 1000
print (f"Completed in {time_diff:.0f} ms.")
