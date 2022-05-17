class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        start = strs[0]

        if len(strs) == 0:
            return ""

        for i in range(1, len(strs)):
            result = ""
            if len(start) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(start) and start[j] == strs[i][j]:
                    result += start[j]
                else:
                    break
            start = result
        return start