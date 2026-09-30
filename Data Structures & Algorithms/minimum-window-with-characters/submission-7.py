class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreq = {}
        for char in t:
            tfreq[char] = tfreq.get(char, 0) + 1
        freq = {char:0 for char in t}
        have = 0
        need = len(tfreq)
        l = 0
        best = float("inf")
        ans = ""
        for r in range(len(s)):
            if s[r] in tfreq:
                freq[s[r]] += 1
                if freq[s[r]] == tfreq[s[r]]:
                    have += 1
            while have == need:
                if r-l+1 < best:
                    best = r-l+1
                    ans = s[l:r+1]
                if s[l] in freq:
                    freq[s[l]] -= 1
                    if freq[s[l]] < tfreq[s[l]]:
                        have -= 1
                l += 1
        return ans
        
            

