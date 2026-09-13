class Solution:
    def convertDateToBinary(self, date: str) -> str:
        a = date.split("-")

        res = ""
        for i in a :
            i = int(i)
            res += bin(i)[2:]
            res += "-"

        return res[:-1]