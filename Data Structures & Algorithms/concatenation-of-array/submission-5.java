class Solution {
    public int[] getConcatenation(int[] nums) {
        ArrayList<Integer> res = new ArrayList<>();
        int idx = 0; 
        for(int i = 0; i < 2; i++){
            for(int j = 0; j < nums.length;j++){
                res.add(nums[j]);
            }
       }
        int[] result = new int[res.size()];
        for(int i = 0; i < res.size(); i++){
            result[i] = res.get(i % res.size()); 
        } 
        return result; 
    }
}