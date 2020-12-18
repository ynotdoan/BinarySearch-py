
class BinarySearch():
  '''
  Sorts and searches for a num using binary search.
  '''
  def __init__(self, k, value):
    self.l = 0
    self.r = len(k) - 1 
    self.mid = (self.l + self.r) // 2
    self.k = k
    self.value = value
    
  def b_search(self):
    '''
    Compares value to mid value and sets new points until value is found.
    '''
    while (self.value != self.k[self.mid]):
      self.mid = (self.l + self.r) // 2
      if (self.value < self.k[self.mid]):
        self.r = self.mid - 1
        
      elif (self.value > self.k[self.mid]):
        self.l = self.mid + 1
        
    if (self.value == self.k[self.mid]):
      print (f"Value {self.value} found at index {self.mid}")
    else:
      print (f"Value {self.value} not found in given list")
