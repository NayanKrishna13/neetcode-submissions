class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        n=len(coins)
        def coin(j,num):
            if (j,num) in cache:
                return cache[(j,num)]

            if num==0:
                return 1
            if j==n:
                return 0
            res=0
            for i in range(j,n):
                if num-coins[i]>=0:
                    #print(i,num-coins[i])
                    res+=coin(i,num-coins[i])
                #print("res:",res)

            cache[(j,num)]=res
            return res
        return coin(0,amount)
            
                

            
         