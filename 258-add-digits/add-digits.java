class Solution {
    public int add(int num){
        int s = 0;
        while(num>0){
            int d = num%10;
            s = s + d;
            num = num/10;
        }
        return s;
    }
    public int addDigits(int num) {
        if(num<10){
            return num;
        }
        int s = 0;
        while(num>9){
            s = add(num);
            num = s;
        }
        return s;
    }
}