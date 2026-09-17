class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        vowels = "aeiou"

        maxy = 0
        maxi = 0

        for i in s :
            if i in vowels :
                maxy = max(maxy, s.count(i))
            else :
                maxi = max(maxi, s.count(i))

        return maxy + maxi