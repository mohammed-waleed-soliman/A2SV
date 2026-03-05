class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        s = intervals[0][0]
        e = intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0]>=s and intervals[i][0]<=e:
                if intervals[i][1]>e:
                    e = intervals[i][1]
            else:
                res.append([s,e])
                s = intervals[i][0]
                e = intervals[i][1]
        res.append([s,e])
        return res