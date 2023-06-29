# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        stck = [(node, 1, 1)]
        dic = {}
        padd, qadd = [], []
        while stck:
            node, lvl, num = stck.pop(0)
            # print(node.val,lvl,num)
            if node == p:
                padd = [lvl, num]
            elif node == q:
                qadd = [lvl, num]
            if qadd and padd:
                break
            num = num*2-1
            if node.left:
                stck.append((node.left, lvl+1, num))
            if node.right:
                stck.append((node.right, lvl+1, num+1))

        if qadd[0] == padd[0]:
            maxnum = 2**(qadd[0]-1)
            if (qadd[1] > maxnum//2 and padd[1] <= maxnum//2) or (qadd[1] > maxnum//2 and qadd[1] <= maxnum//2):
                return root
            lvl = qadd[0]
            while qadd[1] != padd[1]:
                if qadd[1] % 2 == 1:
                    qadd[1] = (qadd[1]//2)+1
                else:
                    qadd[1] = (qadd[1]//2)
                if padd[1] % 2 == 0:
                    padd[1] = padd[1]//2
                else:
                    padd[1] = (padd[1]//2)+1
                lvl -= 1
            ans = [lvl, qadd[1]]
        else:
            maxnumq = 2**(qadd[0]-1)
            maxnump = 2**(padd[0]-1)
            if (qadd[1] > maxnumq//2 and padd[1] <= maxnump//2) or (padd[1] > maxnump//2 and qadd[1] <= maxnumq//2):
                return root
            if qadd[0] > padd[0]:
                while qadd[0] != padd[0]:
                    if qadd[1] % 2 == 1:
                        qadd[1] = (qadd[1]//2)+1
                    else:
                        qadd[1] = (qadd[1]//2)
                    qadd[0] -= 1
            else:
                while padd[0] != qadd[0]:
                    if padd[1] % 2 == 0:
                        padd[1] = padd[1]//2
                    else:
                        padd[1] = (padd[1]//2)+1
                    padd[0] -= 1
            while qadd[1] != padd[1]:
                if qadd[1] % 2 == 1:
                    qadd[1] = (qadd[1]//2)+1
                else:
                    qadd[1] = (qadd[1]//2)
                if padd[1] % 2 == 0:
                    padd[1] = padd[1]//2
                else:
                    padd[1] = (padd[1]//2)+1
                qadd[0] -= 1
            ans = qadd
        # print(ans)
        node = root
        stck = [(node, 1, 1)]
        while stck:
            node, lvl, num = stck.pop(0)
            # print(node.val,lvl,num)
            if [lvl, num] == ans:
                return node
            num = num*2-1
            if node.left:
                stck.append((node.left, lvl+1, num))
            if node.right:
                stck.append((node.right, lvl+1, num+1))
