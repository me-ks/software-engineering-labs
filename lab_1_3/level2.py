from level1 import Student, BinaryTree

class SearchTree(BinaryTree):
    def search_male_3_dorm(self):
        res = []
        self._search(self.root, res)
        return res

    def _search(self, node, res):
        if not node: return
        s = node.data
        if s.gender == "М" and s.course == 3 and s.residence == "гуртожиток":
            res.append(s)
        self._search(node.left, res)
        self._search(node.right, res)

if __name__ == "__main__":
    t = SearchTree()
    t.insert(Student("Сидоренко", "Андрій", 3, 1320, "М", "гуртожиток"))
    t.insert(Student("Бойко", "Василь", 3, 890, "М", "гуртожиток"))
    found = t.search_male_3_dorm()
    t.display(found)