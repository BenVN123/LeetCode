class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for e in range(len(triangle[i])-1, -1, -1):
                triangle[i][e] += min(triangle[i+1][e], triangle[i+1][e+1])
        return triangle[0][0]