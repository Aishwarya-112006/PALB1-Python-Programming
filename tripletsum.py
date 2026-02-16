'''Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.

Return true if such a triplet exists, otherwise, return false.

Examples: 

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
Output: true 
Explanation: The triplet {1, 4, 8} sums up to 13.
Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10
Output: true 
Explanation: The triplets {1, 3, 6} and {1, 2, 7} both sum to 10. 
Input: arr[] = [40, 20, 10, 3, 6, 7], target = 24
Output: false 
Explanation: No triplet in the array sums to 24.'''

class Solution:
    def hasTripletSum(self, arr, target):
      n=len(arr)
      arr.sort()
      for i in range(n-2):
        left=i+2
        right=n-1
        while left<right:
          curr_sum=arr[i]+arr[left]+arr[right]
          if curr_sum==target:
            return True
          elif curr_sum<target:
            left+=1
          else:
            right-=1
    return False

'''Dry Run
arr=[1,4,45,6,10,8]
n=6
arr_sort=[1,4,6,8,10,45]
for i=0 to i=3
i=0 fixed --> arr[0]=1
i=1--> left=4'''
