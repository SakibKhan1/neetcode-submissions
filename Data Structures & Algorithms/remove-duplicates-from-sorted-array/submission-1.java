class Solution {
    public int removeDuplicates(int[] nums) {
        int counter = 1;
        HashSet<Integer> visited = new HashSet<>();  
        for(int i = 1; i < nums.length; i++){
            if(nums[i] == nums[i - 1]) continue; 
            nums[counter] = nums[i];
            counter += 1; 
        }
        return counter; 
    }
}