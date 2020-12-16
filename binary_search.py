
class binary_search():
  def __init__(self, l, r, mid, k, value):
    self.l = 0
    self.r = len(k) - 1
    self.mid = (l + r) / 2
    
  def binary_search(self, l, r, mid, k, value):
    if (value < k[mid]):
      r = mid - 1
      return binary_search(l, r, mid, k, value)
    elif (value > k[mid]):
      l = mid + 1
      return binary_search(l, r, mid, k, value)
    elif (value == k[mid]):
      return True
    
    return -1