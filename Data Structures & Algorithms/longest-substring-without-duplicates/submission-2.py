class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l = 0
        best = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
        return best