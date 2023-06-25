# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(ns, nt):
            if ns == None and nt == None:
                # print("--True")
                return True
            elif ns == None or nt == None:
                # print("--False")
                return False
            elif ns.val == nt.val:
                # print(ns.val)
                return dfs(ns.right, nt.right) and dfs(ns.left, nt.left)
            else:
                # print("--False2")
                return False

        def dfs2(ns, nt):
            if ns == None:
                return False
            else:
                return dfs(ns, nt) or dfs2(ns.right, nt) or dfs2(ns.left, nt)
        return dfs2(s, t)
