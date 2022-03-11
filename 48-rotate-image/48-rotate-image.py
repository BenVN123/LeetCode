class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(int(len(matrix))-1, -1, -1):
            for e in range(len(matrix)):
                matrix[e].append(matrix[i][e])  
                
        for i in range(len(matrix)):
            matrix[i] = matrix[i][len(matrix):]        