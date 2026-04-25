class Solution {
    public int[] getConcatenation(int[] nums) {
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < nums.length; j++) {
                res.add(nums[j]);
            }
        }
        int[] res2 = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            res2[i] = res.get(i);
        }
        return res2;
    }
}