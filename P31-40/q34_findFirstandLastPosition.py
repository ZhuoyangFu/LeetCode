class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search_index(nums, target, sign):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left+right) // 2
                if nums[mid] > target or (sign and target==nums[mid]):
                    right = mid
                else:
                    left = mid + 1

            return left

        left_index = search_index(nums, target, True)

        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]

        right_index = search_index(nums, target, False) - 1
        return [left_index, right_index]