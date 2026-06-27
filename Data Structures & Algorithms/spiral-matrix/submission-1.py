class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        k=0
        ans=[]
        c=0
        i,j=0,0
        while(len(ans)!=n*m):
            if c==0:
                if j<m-k:
                    ans.append(matrix[i][j])
                    j+=1
                else:
                    i+=1
                    j-=1
                    c=1
            elif c==1:
                if i<n-k:
                    ans.append(matrix[i][j])
                    i+=1
                else:
                    j-=1
                    i-=1
                    c=2
            elif c==2:
                if j>=k:
                    ans.append(matrix[i][j])
                    j-=1
                else:
                    i-=1
                    j+=1
                    c=3
            else:
                if i>k:
                    ans.append(matrix[i][j])
                    i-=1
                else:
                    i+=1
                    j+=1
                    k+=1
                    c=0
        return ans

                



        