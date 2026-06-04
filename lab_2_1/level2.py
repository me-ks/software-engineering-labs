import math

EPS = 1e-6

def f(x):
    return x**3 - 2 * math.cos(math.pi * x)

def df(x):
    return 3 * x**2 + 2 * math.pi * math.sin(math.pi * x)

def d2f(x):
    return 6 * x + 2 * math.pi**2 * math.cos(math.pi * x)

def bisection(a, b):
    while (b - a) / 2 > EPS:
        mid = (a + b) / 2
        if f(a) * f(mid) < 0: b = mid
        else: a = mid
    return (a + b) / 2

def newton(a, b):
    x = a if f(a) * d2f(a) > 0 else b
    for _ in range(100):
        xn = x - f(x) / df(x)
        if abs(xn - x) < EPS: return xn
        x = xn
    return x

def chord(a, b):
    for _ in range(100):
        fa, fb = f(a), f(b)
        x = a - fa * (b - a) / (fb - fa)
        if abs(f(x)) < EPS: return x
        if fa * f(x) < 0: b = x
        else: a = x
    return a

def main():
    intervals = [[-1.5, -0.5], [0.5, 1.5], [1.5, 2.5]]
    print("Корені x³ − 2cos(πx) = 0")
    for i, (a, b) in enumerate(intervals):
        print(f"\nКорінь #{i+1} на [{a}, {b}]:")
        print(f"  Бісекція: {bisection(a, b):.6f}")
        print(f"  Ньютон:   {newton(a, b):.6f}")
        print(f"  Хорд:     {chord(a, b):.6f}")

if __name__ == "__main__":
    main()