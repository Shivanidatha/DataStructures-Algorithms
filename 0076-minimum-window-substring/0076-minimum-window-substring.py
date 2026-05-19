class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        l=0
        minlen=float('inf')
        ans=""
        hm={}
        required=0
        for i in range(len(t)):
            hm[t[i]]=hm.get(t[i],0)+1

        hm1={}
        for i in range(len(s)):
            hm1[s[i]]=hm1.get(s[i],0)+1

            if s[i] in hm and hm1[s[i]]==hm[s[i]]:
                required+=1

            while required==len(hm):
                if i-l+1<minlen:
                    ans=s[l:i+1]
                    minlen=i-l+1
                hm1[s[l]]-=1
                if s[l] in hm and hm1[s[l]]< hm[s[l]]:
                    required-=1
                l+=1  
                
        return ans
            