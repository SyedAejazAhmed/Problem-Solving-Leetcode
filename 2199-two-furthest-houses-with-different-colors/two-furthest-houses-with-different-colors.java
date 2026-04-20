class Solution {
    public int maxDistance(int[] colors) {
        int max = 0;
        for(int i=0;i<colors.length/2;i++){
            for(int j=1;j<colors.length;j++){
                if (colors[i] != colors[j]){
                    if (max < j-i){
                        max = j-i;
                    }
                }
            }
        }
        return max;
    }
}