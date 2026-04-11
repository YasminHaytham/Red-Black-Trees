class Node:
    def __init__(self, value):
        self.value = value
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = "BLACK"
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL

    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left: # parent is left
                uncle = node.parent.parent.right
                # Red Uncle
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    # Black Uncle
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else: # parent is right
                uncle = node.parent.parent.left
                # Red Uncle
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    # Black Uncle
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def SearchWord(self, value):
        current = self.root
        while current != self.NIL:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    

    def TreeHight(self, node):
        if node == self.NIL:
            return 0
        else:
            left_height = self.TreeHight(node.left)
            right_height = self.TreeHight(node.right)
            return max(left_height, right_height) + 1
        

    def BlackHeight(self, node):
        if node == self.NIL:
            return 1
        else:
            left_black_height = self.BlackHeight(node.left)
            right_black_height = self.BlackHeight(node.right)
            if node.color == "BLACK":
                return max(left_black_height, right_black_height) + 1
            else:
                return max(left_black_height, right_black_height)
            
    
    def TreeSize(self, node):
        if node == self.NIL:
            return 0
        else:
            left_size = self.TreeSize(node.left)
            right_size = self.TreeSize(node.right)
            return left_size + right_size + 1