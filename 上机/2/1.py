class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        r = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.append([i,j])
       # print(r)      
        for i in r:
            matrix[i[0]] = [0 for _ in range(n)]
        for i in r:
            for j in range(m):
                matrix[j][i[1]] = 0
        
        return matrix