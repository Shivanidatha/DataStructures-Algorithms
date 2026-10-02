class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         idx=[(n,i) for i,n in enumerate(nums)]
         idx.sort(key=lambda x:x[0])
         l=0
         r=len(nums)-1
         while l<r:
            summ=idx[l][0]+idx[r][0]
            if summ==target:
                return [idx[l][1],idx[r][1]]
            elif summ<target:
                l+=1
            else:
                r-=1
         return []
        