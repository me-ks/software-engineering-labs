from collections import Counter

def factorial(n):
    res = 1
    for i in range(2, n + 1): res *= i
    return res

def permutation_with_repetition(word):
    freq = Counter(word)
    n = len(word)
    num = factorial(n)
    den = 1
    for count in freq.values():
        den *= factorial(count)
    return num // den, num, den, freq

def next_permutation(arr):
    a = list(arr)
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]: i -= 1
    if i < 0: return None
    j = len(a) - 1
    while a[j] <= a[i]: j -= 1
    a[i], a[j] = a[j], a[i]
    a[i+1:] = reversed(a[i+1:])
    return "".join(a)

def solve(word):
    res, num, den, freq = permutation_with_repetition(word)
    n = len(word)

    print("\n" + "═"*52)
    print(" Рівень 2 — Перестановки з повтореннями")
    print("═"*52)
    print(f"\nСлово: «{word}», n = {n}")

    print("\n--- Аналіз букв ---")
    for char, count in sorted(freq.items()):
        mark = f" ← повторюється {count} рази" if count > 1 else ""
        print(f"  «{char}» — {count}{mark}")

    print(f"\n--- Обчислення ---")
    print(f"P = {n}! / (добуток факторіалів повторень)")
    print(f"P = {num} / {den} = {res}")

    print("\n--- Приклади (перші 12) ---")
    current = "".join(sorted(word))
    for i in range(1, 13):
        print(f"  {i:2}. {current}")
        current = next_permutation(current)
        if not current: break

if __name__ == "__main__":
    word = input("Введіть слово (Enter для 'програмування'): ").strip() or "програмування"
    solve(word)