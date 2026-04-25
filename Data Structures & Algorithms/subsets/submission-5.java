class Solution {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> curr = new ArrayList<>();
    public void dfs(int i, int[] nums) {
        if (i == nums.length) {
            res.add(new ArrayList<>(curr));
            return;
        }
        curr.add(nums[i]);
        dfs(i + 1, nums);
        curr.remove(curr.size() - 1);
        dfs(i + 1, nums);
    }

    public List<List<Integer>> subsets(int[] nums) {
        dfs(0, nums);
        return res;
    }
}