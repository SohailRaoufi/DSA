from collections import deque
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None




class BST:
    def __init__(self,root):
        self.root = Node(root)
    def insert(self,root,value):
        if root == None:
            return Node(value)
        
        if value > root.value:
            root.right = self.insert(root.right,value)
        elif value < root.value:
            root.left = self.insert(root.left,value)
        
        return root
    
    def get(self,root):
        if root == None:
            return
        
        self.get(root.left)
        print(root.value, end=" ")
        self.get(root.right)
    
    def getMax(self,node):
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

    def search(self,root,key):
        t = root
        while t != None:
            if(t.value == key):
                return t
            elif t.value > key:
                t = t.left
            elif t.value < key:
                t = t.right
        
        return None
        
    def delete(self,root,node):
        if not root:
            return None
        
        if node > root.value:
            root.right = self.delete(root.right,node)
        elif node < root.value:
            root.left = self.delete(root.left, node)
        else:
            if not root.left and not root.right:
                return None
            

            if not root.left:
                return root.right
            if not root.right:
                return root.left
            max_node = self.getMax(root.left)
            root.value = max_node.value
            root.left = self.delete(root.left,max_node.value)

        return root


BT = BST(5)
BT.insert(BT.root,3)
BT.insert(BT.root,8)
BT.insert(BT.root,2)
BT.insert(BT.root,1)
BT.insert(BT.root,6)
BT.insert(BT.root,9)
BT.delete(BT.root,8)
BT.get(BT.root)
print()


