class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        
        evenSum = 0
        oddSum = 0 

        for i in range(len(nums)) :
            if i % 2 == 0 :
                evenSum += nums[i]
            else :
                oddSum += nums[i]

        return (evenSum - oddSum)