#Solution 1
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def dfs(l = 0, r = 0, path = ''):
            if len(path) == 2*n:
                result.append(path)
                return
            if l < n:
                dfs(l + 1, r, path + '(')
            if r < l:
                dfs(l, r + 1, path + ')')
        dfs()
        return result
#Solution 2
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.bt(n, l=0, r=0, path='')

    def bt(self, n, l=0, r=0, path=''):
        res = []
        if l == n and r == n:
            return [path]
        if l < n:
            res.extend(self.bt(n, l+1, r, path+'('))
        if r < l:
            res.extend(self.bt(n, l, r+1, path+')'))
        return res
