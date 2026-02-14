'''You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

Note : A subarray is a continuous part of an array.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.
Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray [-2] has the largest sum -2.
Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.'''
class Solution:
    def maxSubarraySum(self, arr):
      current_sum=arr[0]#2
      max_sum=arr[0]#2
      for i in range(1,len(arr)):#i=1 to 7
        current_sum=max(arr[i],current_sum+arr[i])#max(3,5)=5--> max(-8,-6),max(7,9)
        max_sum=max(current_sum,max_sum)#max(2,5)=5
      return max_sum








































