/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int dfs(TreeNode root){
        if(root == null){
            return 0; 
        }
        int left = dfs(root.left);
        int right = dfs(root.right);
        return Math.max(left, right) + 1; 
    }
    public boolean isBalanced(TreeNode root) {
        if(root == null){
            return true; 
        }
        int left = dfs(root.left);
        int right = dfs(root.right);
        boolean l2 = isBalanced(root.left);
        boolean r2 = isBalanced(root.right);
        if(Math.abs(left - right) > 1){
            return false; 
        }
        if(l2 == true && r2 == true){
            return true;
        }else{
            return false; 
        }
    }
}
