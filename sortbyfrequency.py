'''Given a string s, the task is to arrange the string according to the frequency of each character, in ascending order. If two elements have the same frequency, then they are sorted in lexicographical order.

Examples:

Input: s = "geeksforgeeks"
Output: forggkksseee
Explanation: All the characters with minimum frequency will occur first and the one with same frequency will be arranged lexicographically.
Input: s = "abc"
Output: abc
Explanation: The frequency is one for all characters hence they'll be arranged lexicographically.'''

class Solution:
    def frequencySort(self, s):
        # code here
        
        f={}
        for i in s:
            f[i]=f.get(i,0)+1
        def sort_keys(item):
            return (item[1],item[0])
        ch=sorted(f.items(),key=sort_keys)
        result=[]
        for i ,count in ch:
            result.append(i*count)
            
        return"".join(result)

      '''Dry run
      '''
        
            
            
