class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mapping = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];

            if (mapping.containsKey(difference)) {
                return new int[]{mapping.get(difference), i};
            }

            mapping.put(nums[i], i);
        }

        return null;
    }
}