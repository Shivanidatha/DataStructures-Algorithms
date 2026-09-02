class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=[]
        l1=l2=0
        size=len(nums1)+len(nums2)
        
        first=size//2
        second=size//2+1
        v1=v2=0
        while l1<len(nums1) and l2<len(nums2):
            if nums1[l1]<nums2[l2]:
                res.append(nums1[l1])
                l1+=1
            else:
                res.append(nums2[l2])
                l2+=1
            if len(res)==first:
                v1=res[-1]
            if len(res)==second:
                v2=res[-1]

            
        while l1<len(nums1):
            res.append(nums1[l1])
            l1+=1
            if len(res)==first:
                v1=res[-1]
            if len(res)==second:
                v2=res[-1]
        while l2<len(nums2):
            res.append(nums2[l2])
            l2+=1
            if len(res)==first:
                v1=res[-1]
            if len(res)==second:
                v2=res[-1]
        return v2 if size%2!=0 else (v1+v2)/2
        