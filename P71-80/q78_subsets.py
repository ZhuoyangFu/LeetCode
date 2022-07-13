#Backtrack
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        tmp = []

        def backtrack(tmp, start):
            res.append(tmp)
            for i in range(start, len(nums)):
                backtrack(tmp + [nums[i]], i + 1)

        backtrack(tmp, 0)
        return res