"a valueless binary search tree"


class BinaryTree:
    def __init__(self):       self.tree = EmptyNode()

    def __repr__(self):       return repr(self.tree)

    def lookup(self, value):  return self.tree.lookup(value)

    def insert(self, value): self.tree = self.tree.insert(value)


class EmptyNode:
    def __repr__(self):
        return "*"

    def lookup(self, value):  # fail at the bottom
        return False

    def insert(self, value):
        return BinaryNode(self, value, self)  # add new node at bottom


class BinaryNode:
    def __init__(self, left, value, right):
        self.data, self.left, self.right = value, left, right

    def lookup(self, value):
        if self.data == value:
            return True
        elif self.data > value:
            return self.left.lookup(value)  # look in left
        else:
            return self.right.lookup(value)  # look in right

    def insert(self, value):
        if self.data > value:
            self.left = self.left.insert(value)  # grow in left
        elif self.data < value:
            self.right = self.right.insert(value)  # grow in right
        return self

    def __repr__(self):
        return ('( %s, %s, %s )' %
                (repr(self.left), repr(self.data), repr(self.right)))


if __name__ == '__main__':
    x = BinaryTree()
    # for i in [1, 2, 3, 4, 5, 6, 7]: x.insert(i)
    for i in range(8): print((i, x.lookup(i)), end=' ')
