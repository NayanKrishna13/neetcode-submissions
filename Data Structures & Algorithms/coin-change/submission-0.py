class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        cache={0:0}
        def mincount(num):
            if num in cache:
                return cache[num]
            res=float('inf')
            for x in coins:
                if num-x>=0:
                    res=min(res,1+mincount(num-x))

            cache[num]=res
            return res
        ans=mincount(amount)
        if ans==float('inf'):
            return -1
        else:
            return ans