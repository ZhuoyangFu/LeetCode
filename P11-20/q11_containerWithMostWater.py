#Solution 1
# #Time Complexity: O(n^2)
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         maxwater = 0
#
#         for i in range(len(height)):
#             for j in range(i, len(height)):
#                 water = min(height[i], height[j])*(j-i)
#                 if water > maxwater:
#                     maxwater = water
#
#
#Better Solution
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxwater = 0
        l = 0
        r = len(height)-1

        while l < r:
            water = (r-l) * min(height[l], height[r])
            if water > maxwater:
                maxwater = water
            if height[l] > height[r]:
                r -= 1
            else:
                l +=1

        return maxwater