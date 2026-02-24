'''You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0'''
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
      def dfs(node,current):
        if not node :
          return 0
        current=(current<<1) | node.val
        if not node.left and node.right:
          return current
        return dfs(node.left,current)+dfs(node.right,current)
      return dfs(root,0)



'''Dry Run

tree=[1,0,1,0,1,0,1]
start at root=1
current=0
current=0<<1|1--> 1
'''
