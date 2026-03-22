'''Given an array arr[] of integers and an integer k, select k elements from the array such that the minimum absolute difference between any two of the selected elements is maximized. Return this maximum possible minimum difference.

Examples:

Input: arr[] = [2, 6, 2, 5], k = 3
Output: 1
Explanation: 3 elements out of 4 elements are to be selected with a minimum difference as large as possible. Selecting 2, 2, 5 will result in minimum difference as 0. Selecting 2, 5, 6 will result in minimum difference as 6 - 5 = 1.
Input: arr[] = [1, 4, 9, 0, 2, 13, 3], k = 4
Output: 4
Explanation: Selecting 0, 4, 9, 13 will result in minimum difference of 4, which is the largest minimum difference possible.'''

class Solution:
    def maxMinDiff(self, arr, k):
        # code here
        arr.sort()
        def place(mid):
            count=1
            l=arr[0]
            for i in range(1,len(arr)):
                if arr[i]-l>=mid:
                    count+=1
                    l=arr[i]
                if count>=k:
                    return True
            return False
        low=0
        high=arr[-1]-arr[0]
        ans=0
        while low<=high:
            mid=(low+high)//2
            if place(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
                
        
        
