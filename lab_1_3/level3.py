from level1 import Student, BinaryTree

class DeleteTree(BinaryTree):
    def delete_by_criteria(self):
        ids = []
        self._collect(self.root, ids)
        for student_id in ids:
            self.root = self._delete(self.root, student_id)

    def _collect(self, node, ids):
        if not node: return
        s = node.data
        if s.gender == "М" and s.course == 3 and s.residence == "гуртожиток":
            ids.append(s.studentId)
        self._collect(node.left, ids)
        self._collect(node.right, ids)

    def _delete(self, root, sid):
        if not root: return None
        if sid < root.data.studentId:
            root.left = self._delete(root.left, sid)
        elif sid > root.data.studentId:
            root.right = self._delete(root.right, sid)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            temp = root.right
            while temp.left: temp = temp.left
            root.data = temp.data
            root.right = self._delete(root.right, temp.data.studentId)
        return root

if __name__ == "__main__":
    t = DeleteTree()
    t.insert(Student("Сидоренко", "Андрій", 3, 1320, "М", "гуртожиток"))
    print("До видалення:")
    t.display()
    t.delete_by_criteria()
    print("Після видалення:")
    t.display()