class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        num = len(self.heap) - self.k
        temp = self.heap
        for i in range(num):
            heapq.heappop(temp)
        return temp[0]
