class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        l=0
        ans=0
        for i in range(len(s)):
            if s[i] not in charset:
                charset.add(s[i])
            else:
                while s[i] in charset:
                    charset.remove(s[l])
                    l+=1
                charset.add(s[i])
            ans=max(ans, i-l+1)
        return ans