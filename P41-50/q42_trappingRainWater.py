class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0

        right = [0]*n
        maxR = height[-1]
        for j in range(n-2,-1,-1):
            if height[j] > maxR:
                maxR = height[j]
            right[j] = maxR
        res = 0
        maxL = height[0]
        for i in range(1,n-1,1):
            if height[i] > maxL:
                maxL = height[i]
            elif min(maxL,right[i]) > height[i]:
                res+=min(maxL,right[i]) - height[i]
        return res