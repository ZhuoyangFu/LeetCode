class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        num = len(s) - 1
        while num >= 0 and s[num] == ' ':
            num -= 1
        while num >= 0 and s[num] != ' ':
            result +=1
            num -= 1
        return result