"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = []
        e = []
        for i in intervals:
            s.append(i.start)
            e.append(i.end)
        s.sort()
        e.sort()
        sp = 0
        ep = 0
        curr = 0
        best = 0
        while sp < len(s) and ep < len(e):
            if s[sp] < e[ep]:
                curr += 1
                sp += 1
            else:
                curr -= 1
                ep += 1
            best = max(curr, best)
        return best

        