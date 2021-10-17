
# 递归算法的关键要明确函数的定义，相信这个定义，而不要跳进递归细节
#中序遍历
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

