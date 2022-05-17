class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        new = abs(x)

        while new != 0:
            t = new % 10
            res = res*10 + t
            new = new // 10

        if res >= 2**31 or res <= -2**31:
            return 0

        if x > 0 or x == 0:
            return res
        else:
            return -res