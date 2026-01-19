class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        ans = []
        a,b,temp = None, None, 0
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                if intervals[i][0] > newInterval[1]:
                    break
                if a == None:
                    a = min(intervals[i][0], newInterval[0])
                b = max(intervals[i][1], newInterval[1])
            else:
                ans.append(intervals[i])
            temp = i
        if a == None:
            a = newInterval[0]
        if b == None:
            b = newInterval[1]
        ans.append([a,b])
        if b >= intervals[temp][0]:
            temp+=1
        for j in range(temp, len(intervals)):
            ans.append(intervals[j])
        return ans
