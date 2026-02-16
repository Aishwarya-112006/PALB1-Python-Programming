'''Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

Examples:

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]
Constraints:
1 <= a.size(), b.size() <= 105
1 <= a[i], b[j] <= 106'''
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
      f={}
      for i in a:
        if if in f:
          f[i]+=1
        else:
          f[i]=1
      for i in b:
        if i not in f or f[i]==0:
          return False:
      f[i]-=1

      return False


'''Dry Run
a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
f={11:1,7:2,1:1,13:1,21:1,3:2} counts no of occurrence of element
checking for element in b
for 11 exist in b --> reduce its count in f
for 3 exist in b --> reduce its count in f
for 7exist in b --> reduce its count in f
for 1 exist in b --> reduce its count in f
for 7 exist in b --> reduce its count in f
if all the element in b is reduced once b is subset of a'''
