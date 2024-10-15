class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

targetSum = 22

def dfs(root,sum = 0):
    if root == None:
        return
    sum += root.val
    if sum == targetSum and root.left == None and root.right == None:
        return True
    

    return dfs(root.left,sum) or dfs(root.right, sum)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)


res = dfs(root)
print(res)