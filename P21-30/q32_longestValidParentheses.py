class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        left = 0
        right = 0

        for i in s:
            if i == '(':
                left += 1
            else:
                right += 1
            if left == right:
                l = 2*right
                maxlength = max(maxlength, l)
            elif right > left:
                left = 0
                right = 0

        left = 0
        right = 0

        for i in reversed(s):
            if i == ')':
                right += 1
            else:
                left += 1
            if left == right:
                l = 2*right
                maxlength = max(maxlength, l)
            elif left > right:
                left = 0
                right = 0

        return maxlength