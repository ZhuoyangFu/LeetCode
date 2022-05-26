class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)==1:return nums
        j=len(nums)-1
        while j>0:
            if nums[j-1]>=nums[j]:
                j-=1
            else:break

        if j!=0:
            for i in range(len(nums)-1,j-1,-1):#
                if nums[j-1]<nums[i]:
                    nums[j-1],nums[i]=nums[i],nums[j-1]
                    break

        for ij in range((len(nums)-1-j+1)//2):
            start=j+ij;
            end=len(nums)-1-ij;
            nums[start],nums[end]=nums[end],nums[start]
        return nums