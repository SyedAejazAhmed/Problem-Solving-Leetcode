class Solution {
    public int[] constructTransformedArray(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                result[i] = 0;
            } else {
                int move = nums[i];
                int idx = (i + move) % n;
                if (idx < 0) idx += n;
                result[i] = nums[idx];
            }
        }

        return result;
    }
}
