class Solution:
    def isValid(self, s: str) -> bool:
        q=[]
        for j in range(len(s)):
            if s[j]=="(" or s[j]=="{" or s[j]=="[":
                q.append(s[j])
            else:
                if q:
                    if q[-1]=="(" and s[j]!=")":
                        return False
                    elif q[-1]=="[" and s[j]!="]":
                        return False
                    elif q[-1]=="{" and s[j]!="}":
                        return False
                    else:
                        q.pop()
                else:
                    return False
        
        if not q:
            return True
        else:
            return False

        