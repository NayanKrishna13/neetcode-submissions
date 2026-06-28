class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=0
        for j in range(len(digits)-1,-1,-1):
            if digits[j]!=9:
                digits[j]+=1
                return digits
            else:
                digits[j]=0
                c=1
        if c==1:
            digits=[1]+digits
        return digits
