#Solution1
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i] + nums[i-1]

        return max(nums)

#Solution2
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        max = nums[0]
        cur = 0

        for i in range(0, len(nums)):
            cur = cur + nums[i]

            if cur > max:
                max = cur

            if cur < 0:
                cur = 0

        return max