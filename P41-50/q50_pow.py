class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def mul(num):
            if num == 0:
                return 1
            new = mul(num//2)
            if num % 2 == 0:
                return new*new
            else:
                return new*new*x

        if n >= 0:
            return mul(n)
        else:
            return 1/mul(-n)