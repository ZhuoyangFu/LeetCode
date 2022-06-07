#Use the bin() method to solve this problem
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = int(a, 2) + int(b, 2)
        bin_sum = bin(sum)

        return bin_sum[2:]