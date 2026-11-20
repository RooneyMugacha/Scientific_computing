"""BIT 2118 - Task 19: Numerical optimization (minimum-cost server plan)."""
from scipy.optimize import minimize


def optimise(cA=12, cB=18, kA=100, kB=170, req=1000):
    s = minimize(lambda z: cA * z[0] + cB * z[1], x0=[5, 3], method="SLSQP",
                 bounds=[(0, None), (0, None)],
                 constraints={"type": "ineq", "fun": lambda z: kA * z[0] + kB * z[1] - req})
    best = None
    for a in range(0, 20):
        for b in range(0, 20):
            if kA * a + kB * b >= req:
                c = cA * a + cB * b
                if best is None or c < best[0]:
                    best = (c, a, b, kA * a + kB * b)
    return s, best


print("--- Base program ---")
s, best = optimise()
print("Optimization success:", s.success)
print(f"Type A allocation: {s.x[0]:.3f}")
print(f"Type B allocation: {s.x[1]:.3f}")
print(f"Total capacity: {100 * s.x[0] + 170 * s.x[1]:.2f}")
print(f"Minimum planning cost: {s.fun:.2f}")
print("Best nearby integer solution:", best)

print("\n--- Changed parameters ---")
for label, kw in (("required capacity 1500", dict(req=1500)),
                  ("cost of B cut to 15", dict(cB=15)),
                  ("cost of B raised to 22", dict(cB=22))):
    s, best = optimise(**kw)
    print(f"{label}: continuous A={s.x[0]:.3f}, B={s.x[1]:.3f}, cost {s.fun:.2f} "
          f"| integer best {best}")
