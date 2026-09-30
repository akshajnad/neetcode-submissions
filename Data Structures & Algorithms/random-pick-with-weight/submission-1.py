import random

class Solution:

    def __init__(self, w: List[int]):
        self.list1 = []
        total = 0
        for weight in w:
            total += weight
            self.list1.append(total)
        self.total = total

    def pickIndex(self) -> int:
        num = random.randint(1, self.total)
        l, r = 0, len(self.list1) - 1
        while l < r:
            m = (l + r) // 2
            if self.list1[m] < num:
                l = m + 1
            else:
                r = m

        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()