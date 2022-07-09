class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        first = False
        row = len(matrix)
        column = len(matrix[0])

        for i in range(row):
            if matrix[i][0] == 0:
                first = True
            for j in range(1, column):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(column):
                matrix[0][j] = 0

        if first:
            for i in range(row):
                matrix[i][0] = 0