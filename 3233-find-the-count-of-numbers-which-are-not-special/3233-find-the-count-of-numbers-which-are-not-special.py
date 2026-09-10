class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        n  = int(r**0.5)

        primes = [1] * (n + 1)
        primes[0] = primes[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = 0

        count = 0

        start = int(l**0.5)
        if start * start < l :
            start+=1

        for i in range(start, n + 1):
            if primes[i]:
                count += 1

        return (r - l + 1) - count