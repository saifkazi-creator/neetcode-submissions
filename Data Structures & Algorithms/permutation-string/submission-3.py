class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash1 = {}
        hash2 = {}
        for i in range(len(s1)):
            hash1[s1[i]] = hash1.get(s1[i], 0) + 1
            hash2[s2[i]] = hash2.get(s2[i], 0) + 1
        if hash1 == hash2:
            return True
        r = len(s1)
        while r < len(s2):
            hash2[s2[r]] = hash2.get(s2[r], 0) + 1
            l = r - len(s1)
            hash2[s2[l]] -= 1
            if hash2[s2[l]] == 0:
                del hash2[s2[l]]
            if hash1 == hash2:
                return True
            r += 1
        return False