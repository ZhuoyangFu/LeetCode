# n = 2: 1+1; 2
# n = 3: 1+1+1; 1+2; 2+1
# n = 4: 1+1+1+1；1+2+1；1+1+2；2+1+1
# n = 5: 1+1+1+1+1; 1+2+1+1; 1+1+2+1; 1+1+1+2; 2+1+1+!; 1+2+2; 2+1+2; 2+2+1
#...
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0 for i in range(n+1)]
        result[0] = 1
        result[1] = 1

        for i in range(2, n+1):
            result[i] = result[i-1] + result[i-2]

        return result[n]