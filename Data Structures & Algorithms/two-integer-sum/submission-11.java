class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mapping = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int calc = target - nums[i];
            if(mapping.containsKey(calc)) return new int[]{mapping.get(calc), i};
            mapping.put(nums[i], i);

        }
        return new int[]{}; 
    }
}
