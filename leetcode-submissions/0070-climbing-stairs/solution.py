class Solution(object):
    def climbStairs(self, n):
        s=1
        l=[0]*46
        l[1]=1
        l[2]=2
        for j in range(3,46):
            l[j]=l[j-1]+l[j-2]
        return l[n]
        


        """
        :type n: int
        :rtype: int
        """
        
