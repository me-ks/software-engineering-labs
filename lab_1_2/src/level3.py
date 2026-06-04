import random
from src.level1 import Square
from src.level2 import HashTableLevel2, DELETED

class HashTableLevel3(HashTableLevel2):
    def delete_by_perimeter(self, threshold):
        removed = 0
        for i in range(self.size):
            item = self.table[i]
            if item and item != DELETED and item.perimeter() > threshold:
                print(f"  [-] Видалено з {i} (P={item.perimeter()}): {item}")
                self.table[i] = DELETED
                self.count -= 1
                removed += 1
        print(f"  [i] Видалено всього: {removed}")

def main():
    print("=== Рівень 3: Видалення за периметром ===\n")
    ht = HashTableLevel3(11)
    for _ in range(8):
        sq = Square(random.uniform(0,10), random.uniform(0,10), round(random.uniform(1,12), 2))
        ht.insert(sq)
    ht.display("До видалення")
    ht.delete_by_perimeter(20)
    ht.display("Після видалення")

if __name__ == "__main__":
    main()