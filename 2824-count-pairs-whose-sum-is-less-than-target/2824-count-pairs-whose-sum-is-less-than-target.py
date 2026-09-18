class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        count = 0
        for i in range(len(nums)) :
            a = target - nums[i]
            for j in range(i+1,len(nums)) :
                if nums[j] < a :
                    count +=1

        return count
