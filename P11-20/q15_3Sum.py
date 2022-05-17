class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        if nums == []:
            return result
        elif len(nums) < 3:
            return result

        nums.sort()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]
            left = i + 1
            right = len(nums) -1

            while left < right:
                if nums[left]+nums[right] == -a:

                    result.append([a, nums[left], nums[right]])
                    while (left < right and nums[left] == nums[left + 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right - 1]):
                        right -= 1
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] > -a:
                    right -= 1
                else:
                    left += 1

        return result