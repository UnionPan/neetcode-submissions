class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        # chars = {}
        # for c in s:
        #     if c in chars:
        #         chars[c] += 1
        #     else:
        #         chars[c] = 1