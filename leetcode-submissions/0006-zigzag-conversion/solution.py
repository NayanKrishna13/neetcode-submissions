class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s
        n=len(s)
        l=['']*n
        k=0
        for j in range(numRows):
            i=j
            c=0
            if j==0 or j==numRows-1:
                while(i<n):
                    #print(k,i)
                    l[k]=s[i]
                    i+=2*(numRows-1)
                    k+=1
            else:
                while(i<n):
                    if c==0:
                        l[k]=s[i]
                        i+=2*(numRows-1-j)
                        k+=1
                        c=1
                    else:
                        l[k]=s[i]
                        i+=2*(j)
                        k+=1
                        c=0

        s1=''.join(l)
        return s1

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
