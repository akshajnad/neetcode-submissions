class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1 = sorted(s1)
        for r in range(len(s1), len(s2)+1):
            sub = sorted(s2[l:r])
            if sub == s1:
                return True
            else:
                l += 1
        return False
            