from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)) :
            m = target - nums[i]

            if m in nums :
                index1 = nums.index(m)
                
                if index1 != i :
                    return i,index1
                

            