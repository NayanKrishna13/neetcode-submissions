class Solution:
    from collections import deque
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        ans=[[0]*n for j in range(m)]
        q=deque()
        c=-1
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
        visited=set()
        #print("starting q:",q)
        while(q):
            current=q.popleft()
            visited.add(current)
            if current[0]<m-1:
                if (current[0]+1,current[1]) not in visited:
                    visited.add((current[0]+1,current[1]))
                    q.append((current[0]+1,current[1]))
                    if mat[current[0]+1][current[1]]==1:
                        ans[current[0]+1][current[1]]=1+ans[current[0]][current[1]]
                else:
                    ans[current[0]+1][current[1]]=min(ans[current[0]+1][current[1]],1+ans[current[0]][current[1]])
                    
            if current[0]>0:
                if (current[0]-1,current[1]) not in visited:
                    visited.add((current[0]-1,current[1]))
                    q.append((current[0]-1,current[1]))
                    if mat[current[0]-1][current[1]]==1:
                        ans[current[0]-1][current[1]]=1+ans[current[0]][current[1]]
                else:
                    ans[current[0]-1][current[1]]=min(ans[current[0]-1][current[1]],1+ans[current[0]][current[1]])
            if current[1]<n-1:
                if (current[0],current[1]+1) not in visited:
                    visited.add((current[0],current[1]+1))
                    q.append((current[0],current[1]+1))
                    if mat[current[0]][current[1]+1]==1:
                        ans[current[0]][current[1]+1]=1+ans[current[0]][current[1]]
                else:
                    ans[current[0]][current[1]+1]=min(ans[current[0]][current[1]+1],1+ans[current[0]][current[1]])

            if current[1]>0:
                if (current[0],current[1]-1) not in visited:
                    visited.add((current[0],current[1]-1))
                    q.append((current[0],current[1]-1))
                    if mat[current[0]][current[1]-1]==1:
                        ans[current[0]][current[1]-1]=1+ans[current[0]][current[1]]
                else:
                    ans[current[0]][current[1]-1]=min(ans[current[0]][current[1]-1],1+ans[current[0]][current[1]]) 
            #print("ans:",ans) 
            #print("q:",q)
        
        return ans
        
