class Solution:
    def minDifference(self, arr):
        # code here
        def to_seconds(t):
            h, m, s = map(int, t.split(":"))
            return h * 3600 + m * 60 + s
        
        times = [to_seconds(t) for t in arr]
        
        # sort times
        times.sort()
        
        min_diff = float('inf')
        
        # check adjacent differences
        for i in range(1, len(times)):
            min_diff = min(min_diff, times[i] - times[i - 1])
        
        # check circular difference (midnight wrap)
        min_diff = min(min_diff, 86400 - (times[-1] - times[0]))
        
        return min_diff
