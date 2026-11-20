"""BIT 2118 - Task 4: Floating-point arithmetic and numerical errors."""
import numpy as np


def direct(x):
    return (np.sqrt(1 + x) - 1) / x


def stable(x):
    return 1 / (np.sqrt(1 + x) + 1)       # conjugate form (Goldberg, 1991)


print("--- Base program ---")
s = 0.1 + 0.2
print("0.1 + 0.2 =", repr(s))
print("Exact comparison:", s == 0.3)
print("Tolerance-based comparison:", bool(np.isclose(s, 0.3)))


def errors(true, approx):
    absolute = abs(true - approx)
    return absolute, absolute / abs(true)


a, r = errors(np.sqrt(2), 1.414)
print(f"Absolute error: {a:.8f}")
print(f"Relative error: {r:.8%}")
for x in (1e-4, 1e-8, 1e-12):
    print(f"x={x:.0e}: direct={direct(x):.12f}, stable={stable(x):.12f}")

print("\n--- Changed parameter ---")
for x in (1e-14, 1e-16):
    print(f"x={x:.0e}: direct={direct(x):.12f}, stable={stable(x):.12f}")
a, r = errors(np.sqrt(2), 1.41421)
print(f"Approximation 1.41421 -> absolute error {a:.8f}, relative {r:.8%}")
