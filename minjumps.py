'''You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

For example:

If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.

Examples : 

Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3 
Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 
Input: arr = [1, 4, 3, 2, 6, 7]
Output: 2 
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
Input: arr = [0, 10, 20]
Output: -1
Explanation: We cannot go anywhere from the 1st element.'''
class Solution:
	def minJumps(self, arr):
    n=len(arr)
    if n<=0:
      return 0
    if arr[0]==0:
      return -1
    maxReach=arr[0]
    step=arr[0]
    jump=1
    for i in range(1,n):
      if i ==n-1:
        return jump
    maxReach=max(maxReach,arr[i]+i)
    step-=1
    if step==0:
      jump+=1
      if i>=maxReach:
        return -1
      step=maxReach-i
  return -1


'''Dry run
arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n=11
maxReach=1
step=1
from i=1 to i=n-1(10)
i=1--> arr[1]=3 != 10--> max(1,1+3)-->4-->step=0-->jump=2-->1 not greater or equal to 4-->step=4-1=3--> new range [2,3,4]
i=2--> arr[2]=5 != 10--> max(2,5+1)-->6-->step=1-->jump=2-->1 not greater or equal to 4-->step=4-1=3--> new range [2,3,4]
'''
