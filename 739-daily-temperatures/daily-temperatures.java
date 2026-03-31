class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Stack<Integer> st = new Stack<>();
        for(int i=0;i<temperatures.length;i++){
            while(!st.isEmpty() && temperatures[i]>temperatures[st.peek()]){
                int ind=st.pop();
                res[ind] = i-ind;
            }
            st.push(i);
        }
        return res;
    }
}