class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                if intervals[i][1] <= merged[-1][1]:
                    merge = merged[-1]
                else:
                    merge = [merged[-1][0], intervals[i][1]]
                merged[-1] = merge
            else:
                merged.append(intervals[i])
        return merged