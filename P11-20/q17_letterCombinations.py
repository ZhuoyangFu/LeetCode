#Solution1
from functools import reduce

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []

        if digits == "":
            return result

        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
               '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        result = []
        n = len(digits)

        def bfs(i, res, temp):
            if i == n:
                res.append(temp)
                return
            for num in dic[digits[i]]:
                bfs(i+1, res, temp+num)
        bfs(0, result, "")
        return result

#Solution2
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='':
            return []
        digit_to_str={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        result=['']
        for x in digits:
            tmp=[]
            for y in result:
                for z in digit_to_str[x]:
                    tmp.append(y+z)
            result=tmp

        return result
#Solution3
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
