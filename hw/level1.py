def fmt(x):
    if abs(x - round(x)) < 1e-6:
        return str(int(round(x)))
    return f"{x:.6f}"


def print_matrix(f, name, M):
    f.write(f"{name}:\n")
    for row in M:
        f.write(" ".join(fmt(x) for x in row) + "\n")


def lu_decomposition(A):
    n = len(A)
    L = [[0]*n for _ in range(n)]
    U = [row[:] for row in A]
    P = [[int(i == j) for j in range(n)] for i in range(n)]

    for i in range(n):
        L[i][i] = 1

    for i in range(n):
        
        max_row = max(range(i, n), key=lambda r: abs(U[r][i]))
        if i != max_row:
            U[i], U[max_row] = U[max_row], U[i]
            P[i], P[max_row] = P[max_row], P[i]
            L[i][:i], L[max_row][:i] = L[max_row][:i], L[i][:i]

        for j in range(i+1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]

    return L, U, P


def solve(L, U, P, b):
    n = len(L)

    
    Pb = [sum(P[i][j]*b[j] for j in range(n)) for i in range(n)]

    
    y = [0]*n
    for i in range(n):
        y[i] = Pb[i] - sum(L[i][j]*y[j] for j in range(i))

    
    x = [0]*n
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(U[i][j]*x[j] for j in range(i+1, n))) / U[i][i]

    return x


def main():
    
    A = [
        [9, 2, -5, -9],
        [8, 1, -6, -7],
        [6, 3, 0, -1],
        [9, 3, 6, 8]
    ]
    b = [16, -2, 24, 18]

    L, U, P = lu_decomposition(A)
    x = solve(L, U, P, b)

    with open("level1_output.txt", "w") as f:
        f.write("Варіант 16\n\n")

        f.write("Задана СЛАР:\n")
        f.write("9x1 + 2x2 -5x3 -9x4 = 16\n")
        f.write("8x1 + 1x2 -6x3 -7x4 = -2\n")
        f.write("6x1 + 3x2 + 0x3 -1x4 = 24\n")
        f.write("9x1 + 3x2 + 6x3 + 8x4 = 18\n\n")

        print_matrix(f, "L", L)
        f.write("\n")
        print_matrix(f, "U", U)
        f.write("\n")
        print_matrix(f, "P", P)

        f.write("\nРозв’язок:\n")
        for i, v in enumerate(x):
            f.write(f"x{i+1} = {fmt(v)}\n")


if __name__ == "__main__":
    main()