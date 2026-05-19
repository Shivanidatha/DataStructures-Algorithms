class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hm1={}
        hm={}
        for i in s:
            hm1[i]=hm1.get(i,0)+1
        for j in t:
            hm[j]=hm.get(j,0)+1
        return hm==hm1