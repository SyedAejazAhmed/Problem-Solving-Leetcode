class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        for r in range(rowIndex + 1):
            p = 1
            for i in range(1, r):
                row[i], p = row[i] + p, row[i]
            row.append(1)
        return row