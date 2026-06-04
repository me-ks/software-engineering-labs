class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def insert(self, value, index=None):
        if index is None: index = self.size
        if self.is_full(): return False
        if index < 0 or index > self.size: return False
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1
        return True

    def remove(self, index=None):
        if index is None: index = self.size - 1
        if self.is_empty(): raise Exception("Empty")
        if index < 0 or index >= self.size: raise Exception("Index Error")
        removed = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return removed

    def get(self, index):
        return self.data[index]

    def print_list(self):
        items = [str(self.data[i]) for i in range(self.size)]
        print(f"Список [{self.size} елем.]: [ {' -> '.join(items)} ]")

def main():
    print("Рівень 1: Список (векторний спосіб)\n")
    list_obj = ArrayList(8)
    hex_values = ["1A", "2F", "3C", "B4", "FF", "0D"]
    for val in hex_values: list_obj.insert(val)
    list_obj.print_list()
    list_obj.insert("7E", 2)
    list_obj.print_list()
    list_obj.remove(0)
    list_obj.print_list()
    list_obj.remove(3)
    list_obj.print_list()
    list_obj.remove()
    list_obj.print_list()

if __name__ == "__main__":
    main()