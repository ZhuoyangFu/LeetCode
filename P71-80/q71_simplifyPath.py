class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = [""]

        for i in path.split('/'):
            if i in(".",""):
                continue
            if i == "..":
                if len(res) > 1:
                    res.pop()
            else:
                res.append(i)

        if len(res) == 1:
            return "/"

        return "/".join(res)