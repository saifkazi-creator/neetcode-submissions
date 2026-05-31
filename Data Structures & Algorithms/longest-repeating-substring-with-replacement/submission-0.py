class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):

            # Add current character
            count[s[r]] = 1 + count.get(s[r], 0)

            # Track highest frequency in window
            maxf = max(maxf, count[s[r]])

            # If invalid window, shrink it
            while (r - l + 1) - maxf > k:

                count[s[l]] -= 1
                l += 1

            # Update answer
            res = max(res, r - l + 1)

        return res