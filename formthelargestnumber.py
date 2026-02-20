'''Given an array of integers arr[] representing non-negative integers, arrange them so that after concatenating all of them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

Examples:

Input: arr[] = [3, 30, 34, 5, 9]
Output: 9534330
Explanation: Given numbers are [3, 30, 34, 5, 9], the arrangement [9, 5, 34, 3, 30] gives the largest value.
Input: arr[] = [54, 546, 548, 60]
Output: 6054854654
Explanation: Given numbers are [54, 546, 548, 60], the arrangement [60, 548, 546, 54] gives the largest value.
Input: arr[] = [3, 4, 6, 5, 9]
Output: 96543
Explanation: Given numbers are [3, 4, 6, 5, 9], the arrangement [9, 6, 5, 4, 3] gives the largest value.'''
from functools import cmp_to_key
class Solution:

	def findLargest(self, arr):
    arr=list(map(str,arr))
    def compare(a,b):
      if a+b >b+a:
        return -1
      elif a+b<b+a:
        return 1
      else:
        return 0
      arr.sort(key=cmp_to_key(compare))
      res="".join(arr)
      if arr[0]=="0":
        return "0"
      return res
      
        
