 # Creating tree and postorder traversal


class Node(object):
    def __init__(self, data):
        self.lc = None
        self.rc = None
        self.data = data


class Binary_tree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self.insert1(self.root, data)

    def insert1(self, node, data):
        if data > node.data:
            if node.rc is None:
                new_node = Node(data)
                node.rc = new_node
            else:
                self.insert1(node.rc, data)
        else:
            if node.lc is None:
                new_node = Node(data)
                node.lc = new_node
            else:
                self.insert1(node.lc, data)


    def postorder_traversal(self):
        if self.root is None:
            print('Tree is empty')
        else:
            self.postorder1(self.root)

    def postorder1(self, node):
        if node.lc is not None:
            self.postorder1(node.lc)
        if node.rc is not None:
            self.postorder1(node.rc)
        print(node.data)




bt = Binary_tree()
bt.insert(12)
bt.insert(6)
bt.insert(14)
bt.insert(3)
bt.postorder_traversal()