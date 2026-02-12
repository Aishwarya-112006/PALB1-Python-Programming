'''Given a sorted array of distinct integers and a target value, return the index if the target
is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4'''
n=len(nums)#4
left=0
right=n-1#3
while left<=right:#0<3
  mid=(left+right)//2#mid=0+3//2=1 --> nums[1]=3
  if (nums[mid]==target):#3!=target
    return mid
  elif(nums[mid]<left):#3>0
    left=mid+1
  else:
    right=mid-1
return left
