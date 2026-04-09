class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.length;i++){
            for(int j=0;i<nums.length;j++){
                if(i==j) break;
                if((nums[i]+nums[j]) == target){
                    return new int[] {i,j};
                }
            }
        }
        return null;
    }
}