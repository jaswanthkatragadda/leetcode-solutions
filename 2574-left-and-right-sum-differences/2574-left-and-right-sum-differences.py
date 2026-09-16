class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        listt1 = []
        listt1.append(0)
        listt2 = []
        listt2.append(0)
        sume = 0
        for i in range(n-1):
            sume = nums[i] + sume
            listt1.append(sume)

        sume = 0
        for i in range(n-1,0,-1) :
            sume = sume + nums[i]
            listt2.append(sume)

        listt2 = listt2[::-1]
        res = []

        for i in range(n) :
            res.append(abs(listt1[i]-listt2[i]))

        return res
