#Method1 - Bubble Sort
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums
#Method2 - Index for colors
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            color = nums[k]
            nums[k] = 2
            if color < 2:
                nums[j] = 1
                j += 1
            if color == 0:
                nums[i] = 0
                i += 1
