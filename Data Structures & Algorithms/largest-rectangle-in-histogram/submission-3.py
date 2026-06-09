class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        if n==1:
            return heights[0]
        q=[]
        m=-1
        for j in range(n):
            if j==0:
                q.append(j)
            else:
                while(q and heights[q[-1]]>=heights[j]):
                    k=q.pop()
                    m=max(m,heights[k]*((1 if heights[k]==heights[j] else 0)+j-k+(k-q[-1]-1 if q else k)))
                    #print(q)
                q.append(j)
            #print("q,m:",q,m)
        
        for j in range(len(q)):
            m=max(m,heights[q[j]]*(n-q[j]+(q[j]-q[j-1]-1 if j!=0 else q[j])))
            #print(m)
        return m
                



        