class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash1 = {}
        for i in t:
            hash1[i] = hash1.get(i, 0) + 1

        hash2 = {}
        l = 0
        min_window = ""

        for r in range(len(s)):
            c = s[r]
            hash2[c] = hash2.get(c, 0) + 1

            while all(hash2.get(c, 0) >= hash1[c] for c in hash1):
                window = s[l:r+1]
                if not min_window or len(window) < len(min_window):
                    min_window = window
                hash2[s[l]] -= 1
                l += 1

        return min_window