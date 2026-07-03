class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        if n==1:
            return True
        l=[]
        for j in range(n):
            if s[j].isalnum():
                l.append(s[j].lower())
        i,j=0,len(l)-1
        print(l)
        while(i<j):
            if l[i]!=l[j]:
                return False
            i+=1
            j-=1
        return True