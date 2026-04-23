class Solution:
    def search(self, txt, pat):
        # Write your code here
        n, m = len(txt), len(pat)
        
        if m > n:
            return False
        
        # frequency arrays (26 lowercase letters)
        freq_pat = [0] * 26
        freq_txt = [0] * 26
        
        # fill pat and first window
        for i in range(m):
            freq_pat[ord(pat[i]) - ord('a')] += 1
            freq_txt[ord(txt[i]) - ord('a')] += 1
        
        # check first window
        if freq_pat == freq_txt:
            return True
        
        # slide window
        for i in range(m, n):
            # add new char
            freq_txt[ord(txt[i]) - ord('a')] += 1
            
            # remove old char
            freq_txt[ord(txt[i - m]) - ord('a')] -= 1
            
            if freq_pat == freq_txt:
                return True
        
        return False
