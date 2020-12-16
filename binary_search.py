
class binary_search():
  def __init__(self, k, value):
    self.value = value
    self.k = []
    
  def binary_search(self, k, value):
    left = 0
    right = len(k) - 1
    mid = (left + right) / 2
    
    while (value != k[mid]):
      mid = (left + right) / 2
      
      if (value < k[mid]):
        right = mid - 1
      elif (value > k[mid]):
        left = mid + 1
    
    return -1