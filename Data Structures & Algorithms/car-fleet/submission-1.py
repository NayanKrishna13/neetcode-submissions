class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        l=[]
        for j in range(n):
            l.append([position[j],speed[j]])
        
        l.sort()
        fleet=0
        m=-1
        for j in range(n-1,-1,-1):
            k=(target-l[j][0])/l[j][1]
            if k>m:
                fleet+=1
                m=k
            print(fleet)
        print(l)
        return fleet



        
        