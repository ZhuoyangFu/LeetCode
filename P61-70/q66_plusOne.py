class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        num = 0

        for i in range(len(digits)):
            if i < len(digits) - 1:
                num = (num + digits[i])*10
            if i == len(digits) - 1:
                num = num + digits[i]


        digit = num + 1

        return list(map(int, str(digit)))