import math

def f(x):
    return math.exp(x * x)

def trapezoid(a, b, h):
    n = round((b - a) / h)
    s = (f(a) + f(b)) / 2
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

def rectangles(a, b, h):
    n = round((b - a) / h)
    l, r, m = 0, 0, 0
    for i in range(n):
        x = a + i * h
        l += f(x)
        r += f(x + h)
        m += f(x + h / 2)
    return l * h, r * h, m * h

def simpson(a, b, h):
    n = round((b - a) / h)
    if n % 2 != 0: n += 1
    step = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 != 0 else 2) * f(a + i * step)
    return (step / 3) * s

def main():
    a, b, h = 0.0, 1.0, 0.2
    print(f"Інтегрування e^(x²) на [{a}, {b}], h={h}")
    
    t = trapezoid(a, b, h)
    rl, rr, rm = rectangles(a, b, h)
    s = simpson(a, b, h)
    
    print(f"Трапецій:    {t:.8f}")
    print(f"Прямок. (с): {rm:.8f}")
    print(f"Сімпсона:    {s:.8f}")

if __name__ == "__main__":
    main()