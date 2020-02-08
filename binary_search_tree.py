class Node(object):
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_value):
        self.insert_helper(self.root, new_value)

    def insert_helper(self, current, new_value):
        if current.value > new_value:
            if current.left != None:
                self.insert_helper(current.left, new_value)
            else:
                current.left = Node(new_value)
        else:
            if current.right != None:
                self.insert_helper(current.right, new_value)
            else:
                current.right = Node(new_value)
    def serch(self, find_val):
        return self.search_helper(self.root, find_val)
    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            if current.value > find_val:
                return self.search_helper(current.left, find_val)
            if current.value < find_val:
                return self.search_helper(current.right, find_val)
    def is_bst_satidfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not Node:
                return True

            val = node.value
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(self.root)


bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print(bst.serch(9))
print(bst.serch(14))