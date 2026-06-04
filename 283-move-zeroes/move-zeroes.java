class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0;
        int j = 0;
        while(j<nums.length){
            if(nums[i]!=0 && nums[j]!=0){
                i+=1;
                j+=1;
            }else if(nums[i]==0 && nums[j]!=0){
                nums[i] = nums[j];
                nums[j] = 0;
            }else if(nums[i]==0 && nums[j]==0){
                j+=1;
            }else if(nums[i]!=0 && nums[j]==0){
                i+=1;
            }
        }
    }
}