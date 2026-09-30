class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        pals = []
        s = list(' '.join(s))
        best = 0
        ans = ""
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            pals.append("".join(s[l:r+1]).replace(" ", ""))
            if len(pals[-1]) > best:
                ans = pals[-1]
                best = len(pals[-1])
            
        return ans
        