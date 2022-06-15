class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        r = ''
        while columnNumber > 0:
            m = (columnNumber-1) % 26
            r += chars[m]
            columnNumber = (columnNumber-1) // 26
        return r[::-1]