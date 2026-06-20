class Solution {
    public int[] shuffle(int[] nums, int n) {
        int x=0; int y=n;
        int[] result = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            if(i%2==0){
                result[i] = nums[x];
                x++;
            }else{
                result[i] = nums[y];
                y++;
            }
        }
        return result;
    }
}