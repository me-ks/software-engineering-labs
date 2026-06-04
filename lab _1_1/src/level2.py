class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = StackNode(value)
        node.next = self.top
        self.top = node
        return True

    def pop(self):
        if self.is_empty(): raise Exception("Empty")
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty(): raise Exception("Empty")
        return self.top.data

    def print_stack(self):
        if self.is_empty():
            print("Стек: [ порожній ]")
            return
        current = self.top
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        print(f"Стек (вершина -> дно): [ {' -> '.join(items)} ]")

def main():
    print("Рівень 2: Стек (зв'язний спосіб)\n")
    stack = LinkedStack()
    values = [10, 25, 7, 42, 3, 88]
    for v in values: stack.push(v)
    stack.print_stack()
    print(f"\nВершина: {stack.peek()}")
    for _ in range(3): stack.pop()
    stack.print_stack()
    stack.push(99)
    stack.push(15)
    stack.print_stack()

if __name__ == "__main__":
    main()