class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[0])

        res=0
        lastend=intervals[0][1]

        for start,end in intervals[1:]:
            if lastend> start:
                lastend=min(lastend,end)
                res+=1
            else:
                lastend=end
        return res