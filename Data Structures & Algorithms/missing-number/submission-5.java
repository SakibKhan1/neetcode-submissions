class Solution {
    public int missingNumber(int[] nums) {
        int local = 0;
        int total = 0;

        for (int i : nums) {
            local = local ^ i;
        }

        for (int i = 0; i <= nums.length; i++) {
            total = total ^ i;
        }

        return local ^ total;
    }
}
