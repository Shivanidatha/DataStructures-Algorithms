class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq=[0]*(len(grid)*len(grid)+1)
        a,b=-1,-1
        for row in grid:
            for col in row:
                freq[col]+=1
        for i in range(1,len(grid)*len(grid)+1):
            if freq[i]==2:
                a=i
            if freq[i]==0:
                b=i
        return [a,b]
        