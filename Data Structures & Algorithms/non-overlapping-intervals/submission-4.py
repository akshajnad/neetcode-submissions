class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:       
        intervals.sort(key = lambda i : i[0])
        ans = 0
        i = 1
        while i < len(intervals):
            last = intervals[i-1]
            curr = intervals[i]
            if last[1] > curr[0]:
                if last[1] > curr[1]:
                    intervals.pop(i-1)
                else:
                    intervals.pop(i)
                i -= 1
                ans += 1
            i += 1
        return ans