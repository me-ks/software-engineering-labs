import os
from level1 import combination, generate_combinations

def write_full(file_path, n, k):
    students = [f"Студент_{str(i+1).zfill(2)}" for i in range(n)]
    c_val = combination(n, k)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("═"*60 + "\n")
        f.write(f" Графік чергування — C({n}, {k}) = {c_val} варіантів\n")
        f.write("═"*60 + "\n")
        
        for i, combo in enumerate(generate_combinations(students, k), 1):
            f.write(f"  {i:5}    | {' | '.join(s.ljust(15) for s in combo)}\n")
    return c_val

def write_compact(file_path, n, k):
    ids = list(range(1, n + 1))
    c_val = combination(n, k)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# C({n},{k}) = {c_val} комбінацій\n")
        for i, combo in enumerate(generate_combinations(ids, k), 1):
            f.write(f"{i}: {list(combo)};\n")
    return c_val

def main(n, k):
    print("\n" + "═"*52)
    print(f" Рівень 3 — Запис у файл (n={n}, k={k})")
    print("═"*52)

    full_f = "combinations_full.txt"
    compact_f = "combinations_compact.txt"

    print(f"Запис у {full_f}...")
    cnt1 = write_full(full_f, n, k)
    print(f"✓ Записано {cnt1} рядків")

    print(f"Запис у {compact_f}...")
    cnt2 = write_compact(compact_f, n, k)
    print(f"✓ Записано {cnt2} комбінацій")

if __name__ == "__main__":
    inp = input("n k (Enter для 16 3): ").strip().split()
    n, k = (int(inp[0]), int(inp[1])) if len(inp) == 2 else (16, 3)
    main(n, k)
    