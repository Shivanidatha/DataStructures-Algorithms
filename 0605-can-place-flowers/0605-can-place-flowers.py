class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            pre= 0 if i== 0 else flowerbed[i-1]
            post= 0 if i==len(flowerbed)-1 else flowerbed[i+1]
            if pre==0 and post==0 and flowerbed[i]==0:
                n-=1
                flowerbed[i]=1
           
        return n<=0

