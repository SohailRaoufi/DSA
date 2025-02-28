class Node:
    def __init__(self, value, height):
        self.left = None
        self.value = value
        self.height = height
        self.right = None


class BST:
    # def __init__(self,root):
    #     self.root = Node(value=root, height = 1)
    def nodeHeight(self, node):
        hl = 0
        hr = 0
        if node:
            if node.left:
                hl = node.left.height
            if node.right:
                hr = node.right.height

        # print(f"Node : {node.value} => Height {node.height}")
        # print(f"hl {hl} hr {hr}")
        if hl > hr:
            return hl + 1
        return hr + 1

    def balanceFactor(self, node):
        # print(node.left.height)
        hl, hr = 0, 0
        if node:
            if node.left:
                hl = node.left.height
            if node.right:
                hr = node.right.height
        return hl - hr

    def LLRotation(self, node):
        # make the left child of node root and right child of left should become left child of node.abs
        # we need 3 pointer: node, node -> left, node -> left -> right
        global root
        nodel = node.left
        nodelr = nodel.right

        nodel.right = node
        node.left = nodelr
        node.height = self.nodeHeight(node)
        nodel.height = self.nodeHeight(nodel)

        if node == root:
            root = nodel

        return nodel

    def RRRotation(self, node):
        global root
        noder = node.right
        noderl = noder.left

        noder.left = node
        node.right = noderl

        node.height = self.nodeHeight(node)
        noder.height = self.nodeHeight(noder)

        if node == root:
            root = noder

        return noder

    def LRRotation(self, node):
        global root
        nodel = node.left
        nodelr = nodel.right

        nodel.right = nodelr.left
        node.left = nodelr.right

        nodelr.left = nodel
        nodelr.right = node

        nodel.height = self.nodeHeight(nodel)
        node.height = self.nodeHeight(node)
        nodelr.height = self.nodeHeight(nodelr)

        if node == root:
            root = nodelr
        return nodelr

    def RLRotation(self, node):
        global root
        noder = node.right
        noderl = node.left

        noder.left = noderl.right
        node.right = noderl.left

        noderl.left = node
        noderl.right = noder

        noder.height = self.nodeHeight(noder)
        node.height = self.nodeHeight(node)
        noderl.height = self.nodeHeight(noderl)

        if node == root:
            root = noderl

        return noderl

    def insert(self, root, value):
        if root == None:
            return Node(value=value, height=1)

        if value > root.value:
            root.right = self.insert(root.right, value)
        elif value < root.value:
            root.left = self.insert(root.left, value)

        root.height = self.nodeHeight(root)
        # print(f"Node : {root.value} => Height: {root.height}")

        # Rotation Function for that node
        # if node is 2 means in left and if left of that node is 1 means its LL.
        if self.balanceFactor(root) == 2 and self.balanceFactor(root.left) == 1:
            # print("Got in LL!")
            return self.LLRotation(root)
        # LR
        elif self.balanceFactor(root) == 2 and self.balanceFactor(root.left) == -1:
            return self.LRRotation(root)
        elif self.balanceFactor(root) == -2 and self.balanceFactor(root.right) == -1:
            return self.RRRotation(root)

        elif self.balanceFactor(root) == -2 and self.balanceFactor(root.left) == 1:
            return self.RLRotation(root)

        return root

    def get(self, root):
        if root == None:
            return None

        self.get(root.left)
        print(root.value, end=" ")
        self.get(root.right)

    def getMax(self, node):
        queue = deque([node])
        res = None
        while queue:
            m = 0
            for n in range(len(queue)):
                t = queue.popleft()

                if t.left:
                    queue.append(t.left)
                if t.right:
                    queue.append(t.right)

                if t.value > m:
                    res = t
                    m = t.value

        return res

    def delete(self, root, node):
        if root == None:
            return None

        if root.value > node:
            root.left = self.delete(root.left, node)
        elif root.value < node:
            root.right = self.delete(root.right, node)

        else:
            if not root.left and not root.right:
                return None

            if not root.left:
                return root.right
            if not root.right:
                return root.left
            max_node = self.getMax(root.left)
            root.value = max_node.value
            root.left = self.delete(root.left, max_node.value)

        if self.balanceFactor(root) == 2 and self.balanceFactor(root.left) == 1:
            return self.LLRotation(root)
        elif self.balanceFactor(root) == 2 and self.balanceFactor(root.left) == -1:
            return self.LRRotation(root)
        elif self.balanceFactor(root) == -2 and self.balanceFactor(root.right) == -1:
            return self.RRRotation(root)
        elif self.balanceFactor(root) == -2 and self.balanceFactor(root.left) == 1:
            return self.RLRotation(root)
        elif self.balanceFactor(root) == 2 and self.balanceFactor(root.left) == 0:
            return self.LLRotation(root)
        elif self.balanceFactor(root) == -2 and self.balanceFactor(root.right) == 0:
            return self.RRRotation(root)
        return root


BT = BST()
root = None
root = BT.insert(root, 30)
BT.insert(root, 10)
BT.insert(root, 40)
BT.insert(root, 20)
BT.insert(root, 5)


"""
            30
           /  \
          10  40
         /  \
        5    20


"""

# print(f"root Height {root.height}")
# print(f"left Height {root.left.height}")
# print(f"right Height {root.right.height}")

print(BT.get(root))
BT.delete(root, 40)
print(BT.get(root))
print(root.value)
