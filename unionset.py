class Solution:    
    def findUnion(self, a, b):
        # code here
        union_set=set()
        for i in a:
            union_set.add(i)
        for j in b:
            union_set.add(j)
        return list(union_set)
