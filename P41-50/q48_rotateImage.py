class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        for i in range(length):
            for j in range(i, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(length):
            matrix[i] = matrix[i][::-1]

        return matrix