
class BinarySearch():
  '''
  Sorts and searches for a num using binary search.
  '''
  def __init__(self, k, value):
    # sort k before sending list to binary search
    self.k = sorted(k)
    self.value = value
    self.l = 0
    self.r = len(k) - 1 


  def b_search(self):
    '''
    Compares value to mid value and sets new points until value is found.
    '''
    # while loop continues as long as left is less than right
    while (self.l <= self.r):
      # sets new mid point by finding div 2 of left + right
      mid = (self.l + self.r) // 2
      
      # if value is less than current mid value, new right is mid - 1
      if (self.value < self.k[mid]):
        self.r = mid - 1
      
      # if value is greater than current mid value, new left is mid + 1  
      elif (self.value > self.k[mid]):
        self.l = mid + 1
      
      # if a value that equals to current mid value is found, break from loop
      elif (self.value == self.k[mid]):
        break
    
    # returns True/False depending on if value was found   
    if (self.value == self.k[mid]):
      return True
    else:
      return False
