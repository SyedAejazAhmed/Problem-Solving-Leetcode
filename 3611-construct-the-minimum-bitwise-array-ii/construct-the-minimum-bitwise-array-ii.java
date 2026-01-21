class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int n = nums.size();
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            int N = nums.get(i);
            if ((N & 1) == 0) {
                ans[i] = -1;
                continue;
            }
            int temp = N;
            int trailingOnes = 0;
            while ((temp & 1) == 1) {
                trailingOnes++;
                temp >>= 1;
            }
            int p = trailingOnes - 1;
            ans[i] = N - (1 << p);
        }

        return ans;
    }
}
