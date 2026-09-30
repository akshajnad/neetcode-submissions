class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def simulate(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/speed)
            return hours

        while low <= high:
            mid = (low + high) // 2
            hours = simulate(mid)
            if hours > h:
                low = mid + 1
            else:
                high = mid - 1
        return low

            