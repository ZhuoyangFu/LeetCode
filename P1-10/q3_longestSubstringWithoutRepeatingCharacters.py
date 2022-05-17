class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_index = 0
        last_index = {}
        maxlength = 0

        for i in range(len(s)):
            if s[i] in last_index:
                start_index = max(start_index, last_index[s[i]]+1)

            maxlength = max(maxlength, i-start_index+1)
            last_index[s[i]] = i

        return maxlength