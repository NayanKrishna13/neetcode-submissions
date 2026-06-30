class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=[]
        curr=[]
        intervals.sort()
        for j in range(len(intervals)):
            if j==0:
                curr.append(intervals[j][0])
                curr.append(intervals[j][1])
            else:
                if curr[1]<intervals[j][0]:
                    #print("here")
                    l.append(curr)
                    curr=[intervals[j][0],intervals[j][1]]
                else:
                    curr[0]=min(curr[0],intervals[j][0])
                    curr[1]=max(curr[1],intervals[j][1])
            #print(curr)
        l.append(curr)
        return l


        