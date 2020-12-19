
import time
from binary_search import BinarySearch as BS

# numss = [1, 11, 3, 4, 5, 6, 7, 8, 9, 2, 4]
# res = BS(numss, 2)
# print (res.b_search())

nums = []
for i in range(0, 1_000):
  nums.append(i)
  
start = time.perf_counter()

res = BS(nums, 1001)
print (res.b_search())

time_diff = (time.perf_counter() - start) * 1000
print (f"Completed in {time_diff:.0f} ms.")
