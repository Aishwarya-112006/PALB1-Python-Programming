'''ou are given a circular array nums and an array queries.

For each query i, you have to find the following:

The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
Return an array answer of the same size as queries, where answer[i] represents the result for query i.

 

Example 1:

Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]

Output: [2,-1,3]'''
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        mp = defaultdict(list)

        # store indices
        for i in range(n):
            mp[nums[i]].append(i)

        ans = []

        for q in queries:
            v = mp[nums[q]]

            # only one time present
            if len(v) == 1:
                ans.append(-1)
                continue

            pos = bisect_left(v, q)
            res = float('inf')

            # left neighbor
            left = v[(pos - 1) % len(v)]
            d1 = abs(q - left)
            res = min(res, min(d1, n - d1))

            # right neighbor
            right = v[(pos + 1) % len(v)]
            d2 = abs(q - right)
            res = min(res, min(d2, n - d2))

            ans.append(res)

        return ans
