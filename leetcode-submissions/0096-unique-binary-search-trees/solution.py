class Solution(object):
    def numTrees(self, n):
        l=[0]*20
        l[0]=1
        l[1]=1
        l[2]=2
        l[3]=5
        if n in {1,2,3}:
            return l[n]
        else:
            for j in range(4,20):
                for i in range(j):
                    l[j]+=l[i]*l[j-1-i]
                if j==n:
                    return l[j]

            



        """
        :type n: int
        :rtype: int
        """
        
