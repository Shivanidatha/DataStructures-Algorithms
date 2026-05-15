class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        ans=0
        freq=[0]*26
        maxfreq=0
        for i in range(len(s)):
            freq[ord(s[i])-ord('A')]+=1
            maxfreq=max(maxfreq,freq[ord(s[i])-ord('A')])

            while i-l+1- maxfreq>k:
                freq[ord(s[l])-ord('A')]-=1
                l+=1
            ans=max(ans,i-l+1)
        return ans

