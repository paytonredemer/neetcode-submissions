class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if not s:
            return True

        freq = {}
        for idx in range(len(s)):
            freq[s[idx]] = freq.get(s[idx], 0) + 1
            freq[t[idx]] = freq.get(t[idx], 0) - 1

        for value in freq.values():
            if value != 0:
                return False
        return True

