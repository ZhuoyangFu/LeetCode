class Solution(object):
    def permute(self, nums):
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
        return res