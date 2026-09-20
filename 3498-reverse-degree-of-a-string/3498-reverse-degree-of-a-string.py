class Solution:
    def reverseDegree(self, s: str) -> int:
        
        count = 1
        sume = 0

        for i in s :
            val = 26 - (ord(i) - ord('a'))
            sume += val*count
            count+=1

        return sume