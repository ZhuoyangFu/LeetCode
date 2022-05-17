class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1

        return result