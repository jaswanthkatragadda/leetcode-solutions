class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        
        countEven = 0
        countOdd = 0
        
        for i in nums :
            if i % 2 == 0:
                countEven +=1
            else :
                countOdd +=1

        result = []

        for i in range(countEven) :
            result.append(0)
        for j in range(countOdd) :
            result.append(1)

        return result