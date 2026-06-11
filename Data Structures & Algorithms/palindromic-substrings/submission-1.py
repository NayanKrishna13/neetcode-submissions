class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        def count_from_center(left: int, right: int) -> int:
            count=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            return count

        for i in range(len(s)):
            ans+=count_from_center(i,i)
            ans += count_from_center(i,i+1)
        return ans