class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        longest_len=0
        count=[0]*256

        while r<len(s):
            count[ord(s[r])]+=1
            while l<r and count[ord(s[r])]>1:
                count[ord(s[l])]-=1
                l+=1
            longest_len=max(longest_len, r-l+1)
            r+=1
        return longest_len

