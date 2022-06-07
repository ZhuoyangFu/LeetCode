#Solution1 - Time Limit Exceeded
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x

        left = 1
        right = x

        while left <= right:
            mid = (left + right)//2
            if x >= mid*mid and x <= (mid-1)*(mid-1):
                return mid
            elif x < mid*mid:
                right = mid - 1
            elif x >= (mid+1)*(mid+1):
                left = mid + 1

        return mid

#Solution2
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        root = 0

        if x == 1 or x == 0:
            return x

        while i < x:
            if i*i <= x:
                root = i
            else:
                root = i - 1
                break

            i += 1

        return root