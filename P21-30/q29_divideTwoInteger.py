#Time Limit Exceed
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0

        if dividend == 0:
            return result

        if divisor*dividend > 0:
            while abs(dividend) >= abs(divisor):
                dividend -= divisor
                result += 1
            return result

        if divisor*dividend < 0:
            while abs(dividend) >= abs(divisor):
                dividend += divisor
                result -= 1
            return result

#Correct Solution
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)) else 1
        m = abs(dividend)
        n = abs(divisor)
        if m < n:
            return 0
        res = 0
        while m >= n:
            tmp = n
            cnt = 1
            while m >= (tmp<<2):
                tmp <<= 2
                cnt <<= 2
            res += cnt
            m -= tmp
        if sign==-1:
            return max(-res, -2**31)
        else:
            return min(res, 2**31 - 1)