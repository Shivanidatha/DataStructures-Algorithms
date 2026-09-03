class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2= nums2, nums1
        total= len(nums1)+len(nums2)
        half= total//2

        l=0
        r=len(nums1)
        while True:
            Amid=(l+r)//2
            Bmid=half-Amid
            
            Aleft=nums1[Amid-1] if Amid -1 >=0 else float('-inf')
            Aright=nums1[Amid] if Amid <len(nums1) else float('inf')
            Bleft=nums2[Bmid-1] if Bmid -1 >=0 else float('-inf')
            Bright=nums2[Bmid] if Bmid <len(nums2) else float('inf')

            if Aleft <= Bright and Aright >= Bleft:
                if total % 2:
                    return min(Bright, Aright)
                return (min(Aright,Bright) + max(Aleft,Bleft))/2
            elif Aleft > Bright:
                r= Amid-1
            else:
                l=Amid+1