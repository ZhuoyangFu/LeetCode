class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s

        newlist = ["" for _ in range(numRows)]
        i = 0
        flag = -1

        for l in s:
            newlist[i] += l
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag

        return "".join(newlist)