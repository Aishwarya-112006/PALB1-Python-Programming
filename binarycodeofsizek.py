'''Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.
 '''
seen=set()
code=1<<k
for i in range (len(s)+k-1):
  sub=s[i:i+k]
            if sub not in seen:
                seen.add(sub)
                code-=1
                if(code==0):
                    return True
        return False
'''Dry run 
seen={}
code=1<<1=2
loop--> 0 to 4--> 0,1,2,3
i=0 --> sub=s[0:1]--> 0  not in seen--> seen={0} --> code=2-1=1
i=1 --> sub=s[1:2]--> 1 not in seen--> seen={0,1} --> code=1-1=0
return true

'''
