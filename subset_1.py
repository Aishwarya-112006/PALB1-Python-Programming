'''Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 '''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      res=[]
      def back(start,route):
        res.append(route[:])
        for i in range(start,len(nums)):
                route.append(nums[i])
                back(i+1,route)
                route.pop()
        back(0,[])
        return res

'''Dry Run
nums=[1,2,3]
initial call back(0,[])

res=[[]]
'''
