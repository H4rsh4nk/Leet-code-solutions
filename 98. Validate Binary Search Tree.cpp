/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> nums;
    void Postorder(TreeNode* root){
        if(!root) return;

        if(root->left) 
            Postorder(root->left);

        nums.push_back(root->val);

        if(root->right) 
            Postorder(root->right);
    }

    bool isValidBST(TreeNode* root) {
        Postorder(root);

        for(int i=0; i < nums.size() - 1; i++){
            if(!(nums[i] < nums[i+1]))
                return false;
            // cout << nums[i];/
        }

        return true;
    }
};