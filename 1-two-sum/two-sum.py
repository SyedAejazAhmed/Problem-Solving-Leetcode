class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target-nums[i]
            if a in nums[i+1:]:
                return i, nums[i+1:].index(a)+i+1