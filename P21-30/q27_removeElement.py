class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0

        for i in range(len(nums)):
            if i < len(nums) and nums[i] == val:
                continue
            nums[count] = nums[i]
            count += 1

        return count