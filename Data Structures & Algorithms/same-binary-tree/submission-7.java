class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        return dfs(p, q);
    }

    private boolean dfs(TreeNode p, TreeNode q) {

        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null || p.val != q.val) {
            return false;
        }
        boolean left = dfs(p.left, q.left);
        boolean right = dfs(p.right, q.right);

        if (left && right == true) {
            return true;
        }
        return false;
    }
}