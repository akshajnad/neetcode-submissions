class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        l = 0
        best = 0
        curr = 0
        for r in range(len(s)):
            right = s[r]
            chars[right] = chars.get(right, 0) + 1
            curr += 1
            left = s[l]
            while chars[right] > 1:
                chars[left] -= 1
                l += 1
                left = s[l]
                curr -= 1
            best = max(curr, best)
        return best