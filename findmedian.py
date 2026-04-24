class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
    
        n = len(arr)
     
    # Step 2: Check if number of elements is odd or even
        if n % 2 != 0:
        # Odd case → return middle element
            return arr[n // 2]
        else:
        # Even case → return average of two middle elements
            mid1 = arr[n // 2 - 1]
            mid2 = arr[n // 2]
            return (mid1 + mid2) / 2
