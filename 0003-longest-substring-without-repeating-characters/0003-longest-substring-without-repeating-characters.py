class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        count=set()
        maxlen=0
        while r<len(s):
            if s[r] not in count:
                count.add(s[r])
                maxlen=max(maxlen, r-l+1)

            else:
                while s[r] in count:
                    count.remove(s[l])
                    l+=1
                count.add(s[r])
            r+=1

        return maxlen
        
