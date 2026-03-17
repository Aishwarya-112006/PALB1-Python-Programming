'''After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed since it's a single character.'''

class Solution:
    def compress(self, chars):
        n = len(chars)
        idx = 0
        i = 0
        
        while i < n:
            ch = chars[i]
            count = 0
            
            while i < n and chars[i] == ch:
                i += 1
                count += 1
            
            chars[idx] = ch
            idx += 1
            
            if count > 1:
                for c in str(count):
                    chars[idx] = c
                    idx += 1
        
        return idx
