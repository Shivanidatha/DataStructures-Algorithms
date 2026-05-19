class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        hmt={}
        for i in t:
            hmt[i]=hmt.get(i,0)+1
        hms={}
        l=0
        have=0
        req= len(hmt)
        ans=""
        minlen=float('inf')

        for r in range(len(s)):
            hms[s[r]]=hms.get(s[r],0)+1
            if s[r] in hmt and hmt[s[r]]==hms[s[r]]:
                have+=1
            while have==req:
                if r-l+1< minlen:
                    ans=s[l:r+1]
                    minlen=r-l+1
                hms[s[l]]-=1
                if s[l] in hmt and hms[s[l]]< hmt[s[l]]:
                    have-=1
                l+=1
        return ans
