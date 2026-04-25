class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length; 
        int[] res = new int[n * 2];
        int idx = 0; 
        for(int i = 0; i < 2; i++){
            for(int j: nums){
                res[idx] = j; 
                idx += 1; 
            }
        }
        return res; 
    }
}