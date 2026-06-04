import math
import random

A = 0.6180339887

class Square:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def area(self):
        return round(self.side ** 2, 4)

    def perimeter(self):
        return round(4 * self.side, 4)

    def __str__(self):
        return f"Square(x={self.x:.2f}, y={self.y:.2f}, side={self.side:.2f}, area={self.area()}, perimeter={self.perimeter()})"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        frac = (key * A) % 1
        return math.floor(self.size * frac)

    def insert(self, square):
        key = square.area()
        pos = self.hash_func(key)
        if self.table[pos] is not None:
            print(f"  [!] Позиція {pos} зайнята: {square}")
            return False
        self.table[pos] = square
        print(f"  [+] Додано на позицію {pos}: {square}")
        return True

    def display(self):
        print("\n--- ХЕШ-ТАБЛИЦЯ (Рівень 1) ---")
        for i in range(self.size):
            item = self.table[i]
            print(f"{i:<3} | {str(item.area() if item else '-'):<8} | {item or '[порожньо]'}")

def main():
    print("=== Рівень 1: Без колізій ===\n")
    ht = HashTable(10)
    for _ in range(6):
        sq = Square(random.uniform(0,10), random.uniform(0,10), round(random.uniform(1,20), 2))
        ht.insert(sq)
    ht.display()

if __name__ == "__main__":
    main()