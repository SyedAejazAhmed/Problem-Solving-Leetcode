class Solution {
    public int removeDuplicates(int[] nums) {
        // time : O(n), n = number of elements to loop through
        // space: O(1)

        // i   j
        // 0 1 2
        // [1,1,2]

        // 

        int i = 0;
        int count = 1;
       
        for(int j = 1; j < nums.length; j++) {
            if(nums[i] != nums[j]) {
                i++;
                count++;
                if(i == j) continue;
                nums[i] = nums[j];
            }
        } 

        return count;
    }
}