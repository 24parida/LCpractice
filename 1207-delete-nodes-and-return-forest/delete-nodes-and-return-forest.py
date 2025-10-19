# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        to_delete = set(to_delete)
        roots = set()

        roots.add(root)
        def deleteNodes(node):
            if not node:
                return None

            if node.val in to_delete:
                if node in roots:
                    roots.remove(node)

                if node.right:
                    roots.add(node.right)
                    node.right = deleteNodes(node.right)
                    
                if node.left:
                    roots.add(node.left)
                    node.left = deleteNodes(node.left)
                    
                return None
            
            node.right = deleteNodes(node.right)
            node.left = deleteNodes(node.left)
            return node
        
        deleteNodes(root)
        return list(roots)
            

