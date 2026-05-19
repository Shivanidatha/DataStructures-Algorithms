class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm={}
        for s in strs:
            t=''.join(sorted(s))
            if t not in hm:
                hm[t]=[]
            hm[t].append(s)
                
        return list(hm.values())
        
            