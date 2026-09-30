"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        if not intervals:
            return 0
        intervals.sort(key = lambda i : i.start)
        rooms = []
        rooms.append([intervals[0]])
        for i in range(1, len(intervals)):
            found = False
            curr = intervals[i]
            for room in rooms:
                if room[-1].end <= curr.start:
                    room.append(curr)
                    found = True
                    break
            if not found:
                rooms.append([curr])
        return len(rooms)
        """

        if not intervals:
            return 0

        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        
        s = 0
        e = 0
        count = 0
        best = 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            best = max(count, best)
        
        return best
        