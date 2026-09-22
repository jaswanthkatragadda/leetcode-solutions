class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
         
        listt = []
        curr = 1
        for i in range(n) :
            listt.append(curr)
            if curr*10 <= n :
                curr = curr*10
            else :
                while curr % 10 == 9 or curr + 1 > n :
                    curr = curr//10
                curr += 1
        return listt

        