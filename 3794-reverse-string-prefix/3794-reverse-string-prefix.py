class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        
        a = s[:k]
        a = a[::-1]

        s = s[k:]

        return a+s