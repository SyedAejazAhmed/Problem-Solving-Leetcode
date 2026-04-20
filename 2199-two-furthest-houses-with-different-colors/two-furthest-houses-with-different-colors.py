class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max = 0
        for i in range(len(colors)//2):
            for j in range(1,len(colors)):
                if colors[i] != colors[j]:
                    if max < j-i:
                        max = j-i
        return max