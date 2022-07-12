#Method1 Runtime Error
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0

        for i in range(0,len(nums),2):
            if nums[i] != nums[i+1]:
                res = nums[i]
                break

        return res

#Methos2 XOR
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for i in nums:
            res ^= i

        return res