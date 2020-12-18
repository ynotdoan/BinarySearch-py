
class BinarySearch():
  '''
  Sorts and searches for a num using binary search.
  '''
  def __init__(self, k, value):
    self.l = 0
    self.r = len(k) - 1 
    self.mid = (self.l + self.r) // 2
    self.k = sorted(k)
    self.value = value
    
  def b_search(self):
    '''
    Compares value to mid value and sets new points until value is found.
    '''
    print (self.k)
    while (self.l <= self.r):
      self.mid = (self.l + self.r) // 2
      print (f"{self.k[self.mid]} {self.mid} {self.value}")
      if (self.value < self.k[self.mid]):
        self.r = self.mid - 1
        
      elif (self.value > self.k[self.mid]):
        self.l = self.mid + 1
        
      elif (self.value == self.k[self.mid]):
        break
       
    if (self.value == self.k[self.mid]):
      return True
    else:
      return False
