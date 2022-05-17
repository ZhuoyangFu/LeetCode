# First Time Solution
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         max = 0
#         maxstring = []
#
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 string = s[i:j]
#                 if (string[::-1] == string) and (len(string)>max):
#                     max = len(string)
#                     maxstring = [i,j]
#
#         return s[maxstring[0]:maxstring[1]]
#
# s = Solution()
# a = 'a'
# print(s.longestPalindrome(a))

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        def findLongest(s, l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        for i in range(len(s)):
            s1 = findLongest(s, i, i)
            if len(s1) > len(longest): longest = s1

            s2 = findLongest(s, i, i+1)
            if len(s2) > len(longest): longest = s2

        return longest