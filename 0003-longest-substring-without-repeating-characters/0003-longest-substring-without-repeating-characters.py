class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s)==0:
            return 0
        hm={}
        l=0
        curmax=0
        for r in range(len(s)):
            hm[s[r]]=hm.get(s[r],0)+1
            while l<=r and hm[s[r]]>1:
                hm[s[l]]-=1
                l+=1
            if r-l+1>curmax:
                curmax=r-l+1
        return curmax
            