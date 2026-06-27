class Solution:
    def isHappy(self, n: int) -> bool:

        def helper(n):
            s=0
            while(n>0):
                s+=(n%10)**2
                n=n//10
            return s
        numset=set()
        while(True):
            n=helper(n)
            if n==1:
                return True
            if n in numset:
                return False
            else:
                numset.add(n)
        
            

            

    