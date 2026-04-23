class Solution:
    def frequencySort(self, s):
        # code here
        from collections import Counter
        
        freq = Counter(s)
        
        # sort by (frequency, character)
        sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        
        result = ""
        
        for ch, count in sorted_chars:
            result += ch * count
        
        return result
        
