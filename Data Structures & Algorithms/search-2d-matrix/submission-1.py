class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        def binarysearch1():
            result=-1
            f,l=0,n-1
            while(f<=l):
                mid=f+(l-f)//2
                if (matrix[mid][-1]>=target):
                    result=mid
                    l=mid-1
                else:
                    f=mid+1
            return result
        
        def binarysearch2(i):
            f,l=0,m-1
            while(f<=l):
                mid=f+(l-f)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]<target:
                    f=mid+1
                else:
                    l=mid-1
            return False
        t=binarysearch1()
        if t==-1:
            return False
        else:
            return binarysearch2(t)

