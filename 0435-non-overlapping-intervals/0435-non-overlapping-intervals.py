class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[1])

        res=[intervals[0]]

        for start,end in intervals[1:]:
            lastend=res[-1][1]
            if lastend> start:
                res[-1][1]=min(lastend,end)
            else:
                res.append([start,end])
        return len(intervals)-len(res)