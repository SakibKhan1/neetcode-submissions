class Solution {
    public int singleNumber(int[] nums) {
        int total = 0;

        for (int num : nums) {
            total = total ^ num;
        }

        return total;
    }
}
