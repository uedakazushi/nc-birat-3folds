"""Exact Riccati normalization and homogeneous Ore-chart identities.

Requires Python 3 and SymPy.  No numerical specialization is used.
"""

import sympy as sp

x, t, y, xi, tau = sp.symbols("x t y xi tau")
r1, r2, r3, aa = sp.symbols("r1 r2 r3 aa")
h00, h01, h02, h10, h11, h12 = sp.symbols("h00 h01 h02 h10 h11 h12")
h0 = h00 + h01 * t + h02 * t**2
h1 = h10 + h11 * t + h12 * t**2
f = aa * (x - r1) * (x - r2) * (x - r3)
h = h0 + x * h1
k = x - r3
phi = (x - r1) / k
eta = y / k


def derivation(expression):
    return f * sp.diff(expression, x) + h * sp.diff(expression, t)


def bracket(left, right):
    return sp.factor(derivation(left) * sp.diff(right, y)
                     - sp.diff(left, y) * derivation(right))


F = -aa * xi * ((r3 - r2) * xi + r2 - r1)
H0 = -(h0 + r1 * h1) / (r3 - r1)
H1 = (h0 + r3 * h1) / (r3 - r1)
assert sp.factor(bracket(phi, eta) - F.subs(xi, phi)) == 0
assert sp.factor(bracket(t, eta) - H0 - phi * H1) == 0
assert bracket(phi, t) == 0
inverse_x = (r3 * xi - r1) / (xi - 1)
assert sp.factor(phi.subs(x, inverse_x) - xi) == 0

s1, s2, bb, a0, a1, a2 = sp.symbols("s1 s2 bb a0 a1 a2")
psi = (t - s1) / (t - s2)
inverse_t = (s2 * tau - s1) / (tau - 1)
semisimple = bb * (t - s1) * (t - s2)
kappa = bb * (s1 - s2)
assert sp.factor(sp.diff(psi, t) * semisimple - kappa * psi) == 0
A = ((a0 * (tau - 1)**2
      + a1 * (s2 * tau - s1) * (tau - 1)
      + a2 * (s2 * tau - s1)**2) / (s1 - s2))
pushed_A = (sp.diff(psi, t) * (a0 + a1 * t + a2 * t**2)).subs(t, inverse_t)
assert sp.factor(pushed_A - A) == 0
assert sp.Poly(A, tau).degree() <= 2

Z, X, T, f1, f2, kap = sp.symbols("Z X T f1 f2 kap")
Fh = f2 * X**2 + f1 * X * Z
Hh = a2 * T**2 + a1 * T * Z + a0 * Z**2 + kap * X * T
ell = -(sp.diff(Fh, X) + sp.diff(Hh, T)) / 4
delta_X, delta_T, delta_Z = Fh + X * ell, Hh + T * ell, Z * ell


def homogeneous_derivation(expression):
    return (delta_X * sp.diff(expression, X)
            + delta_T * sp.diff(expression, T)
            + delta_Z * sp.diff(expression, Z))


divergence = sp.diff(delta_X, X) + sp.diff(delta_T, T) + sp.diff(delta_Z, Z)
assert sp.expand(divergence) == 0
assert sp.factor(homogeneous_derivation(X / Z) - Fh / Z) == 0
assert sp.factor(homogeneous_derivation(T / Z) - Hh / Z) == 0
assert sp.factor(homogeneous_derivation(Z) - Z * ell) == 0
assert sp.expand((T * Fh - X * Hh).subs(Z, 0)
                 - X * T * ((f2 - kap) * X - a2 * T)) == 0

# The Ore convention is [a,V]=hbar Delta(a).  Left multiplication by Z^-1
# therefore gives the exact affine chart brackets shown below.
chart_first = sp.factor(homogeneous_derivation(X / Z) / Z)
chart_second = sp.factor(homogeneous_derivation(T / Z) / Z)
assert sp.factor(chart_first - (f2 * (X / Z)**2 + f1 * X / Z)) == 0
assert sp.factor(chart_second
                 - (a2 * (T / Z)**2 + a1 * T / Z + a0 + kap * X * T / Z**2)) == 0

print("Riccati root normalization, semisimple Mobius normalization, divergence,")
print("normal homogeneous Ore chart, and degree-two foliation identities passed.")
