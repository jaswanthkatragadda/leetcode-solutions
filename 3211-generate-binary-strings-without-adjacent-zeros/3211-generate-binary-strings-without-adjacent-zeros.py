class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        listt = []
        for i in range(1<<n) :
            ans = ""
            for j in range(n) :
                if i & (1<<j) :
                    ans+="1"
                else :
                    ans +="0"

            if "00" not in ans :
                listt.append(ans)

        return listt