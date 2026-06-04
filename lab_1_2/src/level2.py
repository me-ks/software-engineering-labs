import math
import random
from src.level1 import Square, A

DELETED = "DELETED"

class HashTableLevel2:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash_func(self, key):
        return math.floor(self.size * ((key * A) % 1))

    def probe(self, base_pos, i):
        return (base_pos + i + i * i) % self.size

    def insert(self, square):
        if self.count >= self.size: return False
        base_pos = self.hash_func(square.area())
        for i in range(self.size):
            pos = self.probe(base_pos, i)
            if self.table[pos] in [None, DELETED]:
                print(f"  [+] Позиція {pos} (крок {i}): {square}")
                self.table[pos] = square
                self.count += 1
                return True
        return False

    def display(self, title="Рівень 2"):
        print(f"\n--- ХЕШ-ТАБЛИЦЯ ({title}) ---")
        for i in range(self.size):
            item = self.table[i]
            print(f"{i:<3} | {item}")

def main():
    print("=== Рівень 2: Квадратичне зондування ===\n")
    ht = HashTableLevel2(10)
    for _ in range(7):
        sq = Square(random.uniform(0,10), random.uniform(0,10), round(random.uniform(1,10), 2))
        ht.insert(sq)
    ht.display()

if __name__ == "__main__":
    main()