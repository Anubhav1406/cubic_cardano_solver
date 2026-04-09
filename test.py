from cubic_cardano_solver import solve_cubic
import mpmath as mp

mp.mp.dps = 50

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        line = input()
        print(line)
        a, b, c, d = [mp.mpc(complex(x)) for x in line.split()]
        if abs(a) == 0:
            print("Not a cubic\n")
            continue
        roots = solve_cubic(a, b, c, d)
        for i, r in enumerate(roots, 1):
            print(f"r{i} = {mp.nstr(r, 10)}")
        print([mp.nstr(abs(a*r**3 + b*r**2 + c*r + d), 10) for r in roots], "\n")
