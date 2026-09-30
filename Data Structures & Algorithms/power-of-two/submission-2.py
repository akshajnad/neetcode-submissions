import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        n = math.log2(n)
        return n == math.floor(n)