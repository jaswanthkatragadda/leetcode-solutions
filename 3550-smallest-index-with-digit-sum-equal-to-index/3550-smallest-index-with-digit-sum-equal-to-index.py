class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)) :
            
            a = nums[i]
            sume = 0
            while a :
                digit = a % 10
                sume+=digit
                a = a//10 

            if sume == i :
                return i

        return -1