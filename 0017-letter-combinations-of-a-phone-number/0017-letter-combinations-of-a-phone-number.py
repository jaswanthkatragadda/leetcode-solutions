class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        res = []
        dictt = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def sol(i,current) :
            
            if len(current) == len(digits) :
                res.append(current) 
                return 

            for c in dictt[digits[i]] :
                sol(i+1,current + c)

        if len(digits) > 0 :
            sol(0, "")

        return res

