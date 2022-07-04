class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for word in strs:
            groupword = tuple(sorted(word))
            res[groupword] = res.get(groupword, []) + [word]

        return list(res.values())