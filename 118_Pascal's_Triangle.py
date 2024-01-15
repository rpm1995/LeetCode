class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        
        pascalsTriangle = [[1], [1,1]]

        for currentRow in range(2, numRows):
            newRow = [1]

            for currentCol in range(1, currentRow):
                newRow.append(pascalsTriangle[currentRow-1][currentCol-1] + pascalsTriangle[currentRow-1][currentCol])
            
            newRow.append(1)
            pascalsTriangle.append(newRow)
        
        return pascalsTriangle
