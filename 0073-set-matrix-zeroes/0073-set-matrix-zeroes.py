class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        new = []
        for row in matrix:
            new.append(row[:])
        for i in range(len(matrix)):
            for j in range (len(matrix[0])):
                if matrix[i][j]==0:
                    for r in range (len(matrix)):
                        new[r][j]=0
                    for c in range (len(matrix[0])):
                        new[i][c]=0
        matrix[:]=new
