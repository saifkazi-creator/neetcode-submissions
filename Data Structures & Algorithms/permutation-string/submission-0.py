class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1={}
        l=0
        r=len(s2)-1
        if len(s1)>len(s2):
            return False
        for i in s1:
            hash1[i]=hash1.get(i,0)+1
        while l + len(s1) <= len(s2):
            hash2={}
            for j in s2[l:l+len(s1)]:
                hash2[j]=hash2.get(j,0)+1
            if hash1==hash2:
                return True
            l+=1
        return False