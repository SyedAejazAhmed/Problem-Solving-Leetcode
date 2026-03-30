class Solution {
public:
    int climbStairs(int n) {
        int i = 1;
        int a = 1;
        int steps = 1;

        while(i < n){
            int b = steps;
            steps = steps + a;
            a = b;
            i++;
        }

        return steps;
    }
};