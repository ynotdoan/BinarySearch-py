nums = [1, 2, 12, 41, 51, 122, 91]
value = 1
print (sorted(nums))

l = 0
r = len(nums) - 1
print (l, r)
mid = (l + r) // 2

while (value != nums[mid]):
  mid = (l + r) // 2
  print (f"mid{mid}")
  if (value < nums[mid]):
    r = mid - 1
    print ("1")
    print (f"index v {nums[mid]}")
    
  elif (value > nums[mid]):
    l = mid + 1
    print ("2")
    print (f"index v {nums[mid]}")

  # elif (value == nums[mid]):
  #   print (nums[mid])
  #   print ("yes")

print (f"***{value} {mid} {nums[mid]}")
print ("yes")
