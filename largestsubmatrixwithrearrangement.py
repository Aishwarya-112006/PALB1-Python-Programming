'''You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

 



'''

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        for i in range (1,m):
            for j in range(n):
                if matrix[i][j]==1:
                    matrix[i][j]+=matrix[i-1][j]
        ans=0
        for row in matrix:
            sorted_row=sorted(row,reverse=True)
            for i in range (n ):
                area=sorted_row[i]*(i+1)
                ans=max(ans,area)
        return ans

        
