
import unittest
import binary_search as b

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 6, 4, 3, 42, 34 ]

class BinarySearchTest(unittest.TestCase):
  '''
  Test cases for class BinarySearch.
  '''
  def setUp(self):
    self.search = b.BinarySearch(nums, 5)
    
  def test_binary_search(self):
    self.search.b_search()
    self.assertTrue(self.search)
    
if __name__ == "__main__":
  unittest.main()
