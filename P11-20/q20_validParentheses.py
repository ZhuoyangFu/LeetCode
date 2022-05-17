class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = []
        map = {')':'(',']':'[','}':'{'}

        for c in s:
            if c in map.values():
                result.append(c)
            elif c in map.keys():
                if result == [] or map[c] != result.pop():
                    return False
            else:
                return True

        return len(result) == 0