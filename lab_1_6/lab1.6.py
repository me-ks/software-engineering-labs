import time
import random

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        node = ListNode(value)
        if not self.head or value < self.head.value:
            node.next = self.head
            self.head = node
        else:
            cur = self.head
            while cur.next and cur.next.value < value:
                cur = cur.next
            node.next = cur.next
            cur.next = node
        self.size += 1

    def linearSearch(self, target):
        cur = self.head
        i = 0
        while cur:
            if cur.value == target: return i
            cur = cur.next
            i += 1
        return -1

    def clear(self):
        self.head = None
        self.size = 0

def linearSearchArray(arr, target):
    for i in range(len(arr)):
        if arr[i] == target: return i
    return -1

def generateArray(n, max_val=1000000):
    return [random.randint(0, max_val) for _ in range(n)]

def avgTime(fn, repeats=5):
    total = 0
    for _ in range(repeats):
        start = time.perf_counter_ns()
        fn()
        total += (time.perf_counter_ns() - start)
    return total // repeats

def nsToMs(ns):
    return round(ns / 1000000, 4)

print("--- РІВЕНЬ 1 ---")
N = 20
sizes1 = [N, N * N, N * N * N]
level1Results = []
for size in sizes1:
    data = generateArray(size)
    lst = SortedLinkedList()
    ns = avgTime(lambda: (lst.clear(), [lst.insert(v) for v in data]), 1)
    print(f"N={size:<8} | {nsToMs(ns):>10} мс")
    level1Results.append((size, nsToMs(ns)))

with open("level1_chart.csv", "w", encoding="utf-8") as f:
    f.write("N,Час вставки (мс)\n")
    for s, ms in level1Results: f.write(f"{s},{ms}\n")

print("\n--- РІВЕНЬ 2 ---")
level2Results = []
for size in sizes1:
    data = generateArray(size)
    lst = SortedLinkedList()
    for v in data: lst.insert(v)
    arr = sorted(data)
    targets = [data[random.randint(0, len(data)-1)] for _ in range(50)]
    nsList = avgTime(lambda: [lst.linearSearch(t) for t in targets])
    nsArr = avgTime(lambda: [linearSearchArray(arr, t) for t in targets])
    print(f"N={size:<8} | Список: {nsToMs(nsList):>8} мс | Масив: {nsToMs(nsArr):>8} мс")
    level2Results.append((size, nsToMs(nsList), nsToMs(nsArr)))

with open("level2_chart.csv", "w", encoding="utf-8") as f:
    f.write("N,Список (мс),Масив (мс)\n")
    for s, l, a in level2Results: f.write(f"{s},{l},{a}\n")

print("\n--- РІВЕНЬ 3 ---")
N3 = 5000
data3 = generateArray(N3)
sorted3 = sorted(data3)
lst3 = SortedLinkedList()
for v in data3: lst3.insert(v)
cases = [("Best", sorted3[0]), ("Average", sorted3[N3 // 2]), ("Worst", -1)]

with open("level3_chart.csv", "w", encoding="utf-8") as f:
    f.write("Випадок,Список (мс),Масив (мс)\n")
    for label, target in cases:
        nsL = avgTime(lambda t=target: lst3.linearSearch(t), 10)
        nsA = avgTime(lambda t=target: linearSearchArray(sorted3, t), 10)
        print(f"{label:<10} | Список: {nsToMs(nsL):>8} мс | Масив: {nsToMs(nsA):>8} мс")
        f.write(f"{label},{nsToMs(nsL)},{nsToMs(nsA)}\n")