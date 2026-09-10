class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == -2147483648 and divisor == -1:
            return 2147483647
            
        sign = 1
        if divisor < 0 and dividend < 0 :
            divisor = abs(divisor)
            dividend = abs(dividend)
            sign = 1
        elif divisor < 0 :
            divisor = abs(divisor)
            sign = -1
        elif dividend < 0 :
            dividend = abs(dividend)
            sign = -1


        result = dividend // divisor
        
        return sign * result 