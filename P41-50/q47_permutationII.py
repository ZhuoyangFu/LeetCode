#Method1
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def iterate(nums = nums, index = 0):
            if index == len(nums) - 1:
                res.append(nums)
            else:
                for i in range(index, len(nums)):
                    nums[i], nums[index] = nums[index], nums[i]
                    iterate(nums[:], index + 1)

        iterate()

        result = []
        for i in res:
            if i not in result:
                result.append(i)

        return result
#Method2
#DFS