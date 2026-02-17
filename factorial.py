'''Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

Examples:

Input: n = 5
Output: [1, 2, 0]
Explanation: 5! = 1*2*3*4*5 = 120'''


class Solution:
    def factorial(self, n):
        result=[1]
        for x in range(2,n+1):
            fact=0
            for i in range(len(result)):
                product=result[i]*x+fact
                result[i]=product%10
                fact=product//10
                
            while fact:
                result.append(fact%10)
                fact//=10
        result.reverse()
        return result
        
                
