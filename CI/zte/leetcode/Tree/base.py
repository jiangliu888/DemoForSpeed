def inorderTraversal(root):
    res =[]
    def dfs(root):
        if not root:
            return 
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)
    dfs(root)
    return res
root = [1,None,2,3]
print(inorderTraversal(root))