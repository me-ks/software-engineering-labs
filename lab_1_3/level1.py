from collections import deque

class Student:
    def __init__(self, lastName, firstName, course, studentId, gender, residence):
        self.lastName = lastName
        self.firstName = firstName
        self.course = course
        self.studentId = studentId
        self.gender = gender
        self.residence = residence

    def __str__(self):
        return f"{self.lastName} {self.firstName} | курс:{self.course} | квиток:{self.studentId} | {self.gender} | {self.residence}"

class TreeNode:
    def __init__(self, student):
        self.data = student
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, student):
        if not self.root:
            self.root = TreeNode(student)
            return True
        curr = self.root
        while True:
            if student.studentId == curr.data.studentId: return False
            if student.studentId < curr.data.studentId:
                if not curr.left: curr.left = TreeNode(student); return True
                curr = curr.left
            else:
                if not curr.right: curr.right = TreeNode(student); return True
                curr = curr.right

    def bfs(self):
        if not self.root: return []
        res, q = [], deque([self.root])
        while q:
            node = q.popleft()
            res.append(node.data)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return res

    def display(self, nodes=None):
        data = nodes if nodes is not None else self.bfs()
        for i, s in enumerate(data, 1):
            print(f"{i}. {s}")

if __name__ == "__main__":
    tree = BinaryTree()
    sts = [Student("Іваненко", "Олег", 2, 1050, "М", "гуртожиток"), 
           Student("Петренко", "Марія", 3, 730, "Ж", "місто")]
    for s in sts: tree.insert(s)
    tree.display()