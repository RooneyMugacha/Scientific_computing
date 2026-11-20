"""BIT 2118 - Task 11: Newton-Raphson and secant methods (IRR of a project)."""
cash = [-10000, 3000, 3500, 4000, 2500]


def make(cf):
    npv = lambda r: sum(c / (1 + r) ** t for t, c in enumerate(cf))
    d = lambda r: sum(-t * c / (1 + r) ** (t + 1) for t, c in enumerate(cf))
    return npv, d


def newton(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for n in range(1, max_iter + 1):
        xn = x - f(x) / df(x)
        if abs(xn - x) < tol:
            return xn, n
        x = xn
    return x, max_iter


def secant(f, x0, x1, tol=1e-10, max_iter=100):
    for n in range(1, max_iter + 1):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2, n
        x0, x1 = x1, x2
    return x1, max_iter


npv, d = make(cash)
print("--- Base program ---")
rn, nn = newton(npv, d, 0.10)
rs, ns = secant(npv, 0.05, 0.20)
print(f"IRR using Newton-Raphson: {rn:.6%}")
print(f"IRR using Secant method: {rs:.6%}")
print(f"NPV at Newton solution: {npv(rn):.6f}")
print(f"Newton iterations: {nn} | Secant iterations: {ns}")

print("\n--- Changed parameters ---")
for inv in (9000, 10000, 12000):
    f, df = make([-inv] + cash[1:])
    print(f"Initial investment {inv}: IRR = {newton(f, df, 0.1)[0]:.4%}")
for x0 in (0.1, 0.5, 1.0):
    r, n = newton(npv, d, x0)
    print(f"Start x0={x0}: IRR={r:.6%} in {n} iterations")
