class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            last = result[len(result)-1]
            curr = intervals[i]
            if last[1] >= curr[0]:
                if last[1] >= curr[1]:
                    newLast = last
                else:
                    newLast = [last[0], curr[1]]
                result.pop(len(result)-1)
                result.append(newLast)
            else:
                result.append(curr)
        return result