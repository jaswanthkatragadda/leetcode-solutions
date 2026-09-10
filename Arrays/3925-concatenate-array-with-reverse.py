class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        
        a = nums[::-1]
        res  = nums + a
        return res