
class binary_search():
  def __init__(self, k, value):
    self.l = 0
    self.r = len(k) - 1
    self.mid = (self.l + self.r) / 2
    self.k = k
    self.value = value
    
  def binary_search(self, l, r, mid, k, value):
    if (value < k[mid]):
      self.r = mid - 1
      binary_search(k, value)
    elif (value > k[mid]):
      self.l = mid + 1
      binary_search(k, value)
    elif (value == k[mid]):
      print ("test")
      return 1
    
    return -1