class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l = 0
        max_length = 0

        for r in range(len(s)):

            # If duplicate exists, shrink window
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # Add current character
            charSet.add(s[r])

            # Update answer
            max_length = max(max_length, r - l + 1)

        return max_length