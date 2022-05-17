#Solution 1 - Time Limited Exceeded
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        if len(nums) < 4:
            return result

        nums.sort()
        n = len(nums)

        for i in range(0, n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(k+1, n):
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            result.append([nums[i],nums[j],nums[k],nums[l]])

        res = []
        for one in result:
            if one not in res:
                res.append(one)

        return res
#Solution 2 - Use Hash
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        if len(nums) < 4:
            return result

        nums.sort()

        d = {}
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum2 = nums[i]+nums[j]
                if sum2 not in d:
                    d[sum2] = [[i,j]]
                else:
                    d[sum2].append([i,j])

        res = []
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                x = target - (nums[i] + nums[j])
                if x in d:
                    for (m,n) in d[x]:
                        if m > j and [nums[i],nums[j],nums[m],nums[n]] not in res:
                            res.append([nums[i],nums[j],nums[m],nums[n]])
        return res
# Solution 3 - Best Solution
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #Solution on the Internet - Iteration
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results