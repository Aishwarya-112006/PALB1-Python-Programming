class Solution:

    def findMinDiff(self, arr,M):

        # code here
        if M>len(arr):
            return -1
        arr.sort()
        min_diff=arr[M-1]-arr[0]
        for i in range(len(arr)-M+1):
            diff=arr[i+M-1]-arr[i]
            min_diff=min(min_diff,diff)
        return min_diff
