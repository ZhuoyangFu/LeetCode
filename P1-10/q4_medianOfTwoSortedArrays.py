class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p = len(nums1)+len(nums2)
        newlist = []
        i = j = 0

        for k in range(0,p):
            if j == len(nums2) or (i < len(nums1) and nums1[i]<=nums2[j]):
                newlist.append(nums1[i])
                i = i + 1
            else:
                newlist.append(nums2[j])
                j = j + 1

        half = p // 2
        if p % 2 == 0:
            return (newlist[half-1]+newlist[half])/2
        else:
            return newlist[half]

s = Solution()
a = [1, 2]
b = [3, 4]
print(s.findMedianSortedArrays(a, b))