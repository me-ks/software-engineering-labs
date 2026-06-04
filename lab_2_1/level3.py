import math

def f(x, y):
    return math.cos(x) - y

def exact(x, x0, y0):
    c = (y0 - (math.sin(x0) + math.cos(x0)) / 2) * math.exp(x0)
    return (math.sin(x) + math.cos(x)) / 2 + c * math.exp(-x)

def rk2(x0, y0, x_end, h):
    x, y = x0, y0
    res = [(x, y, exact(x, x0, y0))]
    while x < x_end - 1e-10:
        if x + h > x_end: h = x_end - x
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y += (k1 + k2) / 2
        x += h
        res.append((x, y, exact(x, x0, y0)))
    return res

def main():
    x0, y0, xe, h = 0, 1, 2, 0.2
    print(f"ДР dy/dx = cos(x)-y, y({x0})={y0}")
    print(f"{'x':>5} | {'y (RK2)':>10} | {'y (Exact)':>10} | {'Error':>10}")
    for x, y, ye in rk2(x0, y0, xe, h):
        print(f"{x:5.1f} | {y:10.6f} | {ye:10.6f} | {abs(y-ye):10.2e}")

if __name__ == "__main__":
    main()