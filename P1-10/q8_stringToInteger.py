# Solution1 - Have problem
# class Solution(object):
#     def myAtoi(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         i = 0
#         number = 0
#         sign = 1
#         INT_MAX, INT_MIN = 2**31-1, -2**31
#
#         while(s[i] == '0'):
#             i = i + 1
#
#         if (s[i] == '-'):
#             sign = -1
#             i = i + 1
#         else:
#             sign = 1
#
#         while (i < len(s) and s[i] >= '0' and s[i] <= '9'):
#             number = number*10 + (ord(s[i])-ord('0'))
#             i = i + 1
#
#         result = number*sign
#
#         if result > INT_MAX:
#             return INT_MAX
#         if result < INT_MIN:
#             return INT_MIN
#
#         return result
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31-1
        INT_MIN = -2**31

        s = s.lstrip()
        i = 0

        isNegative = len(s) > 1 and s[0] == '-'
        isPositive = len(s) > 1 and s[0] == '+'
        if isNegative:
            i += 1
        elif isPositive:
            i += 1

        result = 0
        while i < len(s) and '0' <= s[i] <= '9':
            result = result * 10 + (ord(s[i]) - ord('0'))
            i += 1

        if isNegative:
            result = -result

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result