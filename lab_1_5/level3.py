from level2 import Student, TreeNode

class SplayBST:
    def __init__(self):
        self.root = None

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, node, key):
        if not node or node.data.record_book_id == key: return node

        if key < node.data.record_book_id:
            if not node.left: return node
            if key < node.left.data.record_book_id:
                node.left.left = self._splay(node.left.left, key)
                node = self._rotate_right(node)
            elif key > node.left.data.record_book_id:
                node.left.right = self._splay(node.left.right, key)
                if node.left.right: node.left = self._rotate_left(node.left)
            return self._rotate_right(node) if node.left else node
        else:
            if not node.right: return node
            if key > node.right.data.record_book_id:
                node.right.right = self._splay(node.right.right, key)
                node = self._rotate_left(node)
            elif key < node.right.data.record_book_id:
                node.right.left = self._splay(node.right.left, key)
                if node.right.left: node.right = self._rotate_right(node.right)
            return self._rotate_left(node) if node.right else node

    def insert(self, student):
        if not self.root:
            self.root = TreeNode(student)
            return
        self.root = self._splay(self.root, student.record_book_id)
        if self.root.data.record_book_id == student.record_book_id: return
        
        new_node = TreeNode(student)
        if student.record_book_id < self.root.data.record_book_id:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    def search(self, key):
        if not self.root: return None
        self.root = self._splay(self.root, key)
        return self.root.data if self.root.data.record_book_id == key else None

if __name__ == "__main__":
    stree = SplayBST()
    stree.insert(Student("Мельник", "Оксана", 101, "Ж", 1600))
    stree.insert(Student("Харченко", "Дмитро", 106, "М", 310))
    print(f"Корінь після вставки 310: {stree.root.data.record_book_id}")
    stree.search(1600)
    print(f"Корінь після пошуку 1600: {stree.root.data.record_book_id}")