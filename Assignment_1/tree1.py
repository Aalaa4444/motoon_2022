
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node , data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node


    def search(self, node, data):
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)



    def deleteNode(self,node,data):
        if node is None:
            return None
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else: # node to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return  temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node

    def traverseInorder(self, root):
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data)
            self.traverseInorder(root.right)

def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    print(root)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print("Traverse Inorder")
    tree.traverseInorder(root)


main()
"""

"""
class QNode :
	def __init__(self, node) :
		self.data = node
		self.next = None
	
class TreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None
	

class MyQueue :
	def __init__(self) :
		self.head = None
		self.tail = None
		self.count = 0
	
	def size(self) :
		return self.count
	
	def isEmpty(self) :
		return self.count == 0
	
	def enqueue(self, value) :
		node = QNode(value)
		if (self.head == None) :
			self.head = node
		else :
			self.tail.next = node
		self.count += 1
		self.tail = node

	def dequeue(self) :
		if (self.head == None) :
			return
		
		self.head = self.head.next
		self.count -= 1
		if (self.head == None) :
			self.tail = None

	def peek(self) :
		if (self.head == None) :
			return None
		
		return self.head.data
	

class BinaryTree :
	def __init__(self) :
		self.root = None
	
	def levelOrder(self) :
		if (self.root != None) :
			q = MyQueue()
			q.enqueue(self.root)
			node = self.root
			while (q.isEmpty() == False and node != None) :
				if (node.left != None) :
					q.enqueue(node.left)
				
				if (node.right != None) :
					q.enqueue(node.right)
				
				print(node.data, end = "  ")
				q.dequeue()
				node = q.peek()
			
		else :
			print("Empty Tree")
		
	

def qtmain() :
	tree = BinaryTree()
	
	#         1
	#       /   \
	#      2     3
	#     /     / \
	#    4     5   6
	#   /     / \
	#  7     8   9
	tree.root = TreeNode(1)
	tree.root.left = TreeNode(2)
	tree.root.right = TreeNode(3)
	tree.root.right.right = TreeNode(6)
	tree.root.right.left = TreeNode(5)
	tree.root.left.left = TreeNode(4)
	tree.root.left.left.left = TreeNode(7)
	tree.root.right.left.left = TreeNode(8)
	tree.root.right.left.right = TreeNode(9)
	tree.levelOrder()
print("tree implement with queue")
qtmain()
