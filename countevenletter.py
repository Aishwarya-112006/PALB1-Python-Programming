class Solution:
    def count(self, s):
        # code here
        freq = {}
        
        # count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        count = 0
        
        # count even frequencies
        for val in freq.values():
            if val % 2 == 0:
                count += 1
        
        return count
