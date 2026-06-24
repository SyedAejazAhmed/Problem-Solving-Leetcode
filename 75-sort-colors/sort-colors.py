class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c1,c2,c3 = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                c1+=1
            elif nums[i] == 1:
                c2+=1
            else:
                c3+=1
        idx = 0
        for i in range(c1):
            nums[idx] = 0
            idx+=1

        for i in range(c2):
            nums[idx] = 1
            idx+=1

        for i in range(c3):
            nums[idx] = 2
            idx+=1
        return nums