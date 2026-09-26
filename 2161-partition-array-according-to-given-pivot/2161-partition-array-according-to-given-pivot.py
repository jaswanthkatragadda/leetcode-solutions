class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        
        res = []

        for i in nums :
            if i < pivot :
                res.append(i)

        c = nums.count(pivot) 
        for i in range(c) :
            res.append(pivot)

        for i in nums :
            if i > pivot :
                res.append(i)

        return res