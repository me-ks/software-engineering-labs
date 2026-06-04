from level1 import Student

class TreeNode:
    def __init__(self, student):
        self.data = student
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def _insert_root(self, node, student):
        if not node: return TreeNode(student)
        if student.record_book_id < node.data.record_book_id:
            node.left = self._insert_root(node.left, student)
            node = self._rotate_right(node)
        else:
            node.right = self._insert_root(node.right, student)
            node = self._rotate_left(node)
        return node

    def insert(self, student):
        self.root = self._insert_root(self.root, student)

    def search(self, id):
        cur = self.root
        while cur:
            if id == cur.data.record_book_id: return cur.data
            cur = cur.left if id < cur.data.record_book_id else cur.right
        return None

if __name__ == "__main__":
    bst = BST()
    bst.insert(Student("Бойко", "Василь", 104, "М", 890))
    bst.insert(Student("Харченко", "Дмитро", 106, "М", 310))
    found = bst.search(890)
    print(f"Знайдено: {found.last_name if found else 'Ні'}")