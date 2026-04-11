import RedBlackTree

def load_dictionary(file_path):
    tree = RedBlackTree.RedBlackTree()
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            tree.insert(word)
    return tree

