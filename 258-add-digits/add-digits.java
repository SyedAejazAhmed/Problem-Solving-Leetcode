class Solution {
    public int addDigits(int num) {
        if(num<10){
            return num;
        }
        int d = num%10;
        num = num/10;
        int ans = addDigits(num);
        return addDigits(ans+d);
        
    }
}