class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix)==0:
            return res
        m = len(matrix)
        n = len(matrix[0])
        k = 0
        l = 0
        last_row = m-1
        last_col = n-1



        while k <= last_row and l <= last_col:
            for i in range(l,last_col+1):
                res.append(matrix[k][i])
            k += 1

            for i in range(k,last_row+1):
                res.append(matrix[i][last_col])
            last_col -= 1

            if(k<=last_row):
                for i in range(last_col,l-1,-1):
                    res.append(matrix[last_row][i])
                last_row -= 1


            if(l<=last_col):
                for i in range(last_row,k-1,-1):
                    res.append(matrix[i][l])
                l += 1

        return res
