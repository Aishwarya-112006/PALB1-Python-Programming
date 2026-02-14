'''Given an array arr, rotate the array by one position in clockwise direction.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.
Input: arr[] = [9, 8, 7, 6, 4, 2, 1, 3]
Output: [3, 9, 8, 7, 6, 4, 2, 1]
Explanation: After rotating clock-wise 3 comes in first position.'''
class Solution:
    def rotate(self, arr):
      if len(arr)==0:
        return arr
      last=arr[-1]#last =5
      for i in range(len(arr)-1,0,-1):#4 to 1
        arr[i]=arr[i-1]#arr[4]=arr[3] ,arr[3]=arr[2],arr[2]=arr[1],arr[1]=arr[0] --> arr=[1,2,3,4,5]
      arr[0]=last 
      return arr#arr=[5,1,2,3,4]
