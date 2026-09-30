class MedianFinder:

    def __init__(self):
        self.small = [] #max
        self.big = [] #min
        self.size = 0
        self.med = None

    def addNum(self, num: int) -> None:
        self.size += 1
        if self.med is None:
            self.med = num
            heapq.heappush(self.small, num * -1)
        else:
            if num >= self.med:
                heapq.heappush(self.big, num)
            else:
                heapq.heappush(self.small, num * -1)
            if len(self.small) > len(self.big):
                if len(self.small)-len(self.big) > 1:
                    heapq.heappush(self.big, -1 * heapq.heappop(self.small))
                if self.size % 2 == 1:
                    self.med = -self.small[0]
                else:
                    self.med = (-self.small[0] + self.big[0])/2
            elif len(self.big) > len(self.small):
                if len(self.big)-len(self.small) > 1:
                    heapq.heappush(self.small, -1 * heapq.heappop(self.big))
                if self.size % 2 == 1:
                    self.med = self.big[0]
                else:
                    self.med = (-self.small[0] + self.big[0])/2
            else:
                self.med = (-self.small[0] + self.big[0])/2

    def findMedian(self) -> float:
        return self.med
        