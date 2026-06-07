class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1,d2={},{}
        def checkperm():
            for j in d1.keys():
                if (j not in d2) or (d1[j]!=d2[j]):
                    return False
            return True
            
        if len(s2)<len(s1):
            return False
        for j in range(len(s1)):
            if s1[j] in d1:
                d1[s1[j]]+=1
            else:
                d1[s1[j]]=1
        
        i,j=0,0
        n1,n2=len(s1),len(s2)

        while(j<n2):
            if s2[j] in d2:
                d2[s2[j]]+=1
            else:
                d2[s2[j]]=1

            if j>=n1-1:
                if j!=n1-1:
                    d2[s2[i]]-=1
                    i+=1
                if checkperm():
                    return True
            j+=1
            #print("d1,d2:",d1,d2)
        return False


        




        