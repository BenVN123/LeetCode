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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> values = new ArrayList<>();
        return helper(root, values);
    }   
    
    private static List<Integer> helper(TreeNode node, List<Integer> list) {
        if (node == null) {
            return list;
        }
        
        helper(node.left, list);
        list.add(node.val);
        helper(node.right, list);
        
        return list;
    }
}