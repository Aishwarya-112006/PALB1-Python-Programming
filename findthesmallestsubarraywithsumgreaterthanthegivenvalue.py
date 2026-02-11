'''Given a number x and an array of integers arr, find the smallest subarray with sum
greater than the given value. If such a subarray do not exist return 0 in that case.
Examples:
Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
Output: 3
Explanation: Minimum length subarray is [4, 45, 6]
Input: x = 100, arr[] = [1, 10, 5, 2, 7]
Output: 0
Explanation: No subarray exist'''
n=len(arr)
min_len=n+1
start=0
current_sum=0
for i in range(n):
  current_sum+=arr[start]
  while current_sum>x:
    
