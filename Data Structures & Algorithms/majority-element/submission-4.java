class Solution {
    public int majorityElement(int[] nums) {
        int sum = 0; 
        int n = nums.length / 2; 
        HashMap<Integer, Integer> mapping = new HashMap<>(); 
        for(int i = 0; i < nums.length; i++){
            mapping.put(nums[i], mapping.getOrDefault(nums[i], 0) + 1);
        }
        for(Integer key: mapping.keySet()){
            if(mapping.get(key) > n){
                return key;
            }
        } 
        return -1; 
    }

}