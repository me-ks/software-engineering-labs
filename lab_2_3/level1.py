import math

def factorial(n):
    if n < 0: raise ValueError("n < 0")
    res = 1
    for i in range(2, n + 1): res *= i
    return res

def combination(n, k):
    if k > n: return 0
    if k == 0 or k == n: return 1
    if k > n - k: k = n - k
    num, den = 1, 1
    for i in range(k):
        num *= (n - i)
        den *= (i + 1)
    return num // den

def arrangement(n, k):
    if k > n: return 0
    res = 1
    for i in range(n - k + 1, n + 1): res *= i
    return res

def generate_combinations(arr, k, start=0, current=None):
    if current is None: current = []
    if len(current) == k:
        yield list(current)
        return
    for i in range(start, len(arr) - (k - len(current)) + 1):
        current.append(arr[i])
        yield from generate_combinations(arr, k, i + 1, current)
        current.pop()

def solve(n, k):
    print("\n" + "═"*52)
    print(" Рівень 1 — Комбінаторна задача (Комбінації)")
    print("═"*52)
    print(f"\nУмова: n = {n} (студентів), k = {k} (чергують)")
    print("Тип: КОМБІНАЦІЯ без повторень C(n, k)")

    c_val = combination(n, k)
    a_val = arrangement(n, k)

    print(f"\n--- Обчислення ---")
    print(f"Формула: C({n},{k}) = {n}! / ({k}! * {n-k}!)")
    print(f"Результат: {c_val}")

    print(f"\n--- Порівняння ---")
    print(f"C({n},{k}) (порядок неважливий): {c_val}")
    print(f"A({n},{k}) (порядок важливий):   {a_val}")

    students = [f"С{i+1}" for i in range(n)]
    combos = []
    gen = generate_combinations(students, k)
    for _ in range(10):
        try: combos.append(next(gen))
        except StopIteration: break

    print(f"\n--- Перші 10 із {c_val} варіантів ---")
    for i, combo in enumerate(combos, 1):
        print(f"  {i:3}. {{ {', '.join(combo)} }}")

if __name__ == "__main__":
    inp = input("n k (Enter для 16 3): ").strip().split()
    n, k = (int(inp[0]), int(inp[1])) if len(inp) == 2 else (16, 3)
    solve(n, k)