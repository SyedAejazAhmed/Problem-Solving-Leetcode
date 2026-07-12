class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        first,last = -1,-1
        while l<=r:
            if nums[l]==target and nums[r]==target:
                first = l
                last = r
                break
            elif nums[l]<target:
                l+=1
            else: #nums[r]>target:
                r-=1
        return first,last
            