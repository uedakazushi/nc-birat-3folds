"""Exact checks for the rational Poisson forms and the logarithmic quantum link.

Requires Python 3 and SymPy.  All identities are over rational function fields
in the displayed symbolic parameters.  AS regularity uses the cited Ore theorem.
"""

from itertools import combinations
import sympy as sp


def poisson_bracket(left, right, variables, brackets):
    result = 0
    for i, j in combinations(range(len(variables)), 2):
        result += brackets[i, j] * (
            sp.diff(left, variables[i]) * sp.diff(right, variables[j])
            - sp.diff(left, variables[j]) * sp.diff(right, variables[i])
        )
    return sp.factor(result)


def check_coordinates(variables, brackets, coordinates, expected):
    for i, j in combinations(range(len(variables)), 2):
        actual = poisson_bracket(coordinates[i], coordinates[j], variables, brackets)
        assert sp.simplify(actual - expected[i, j]) == 0, (i, j, actual)


u, v, w, z, a, b, lam, mu, kappa = sp.symbols("u v w z a b lam mu kappa")
r1, r2, beta = sp.symbols("r1 r2 beta")
A = sp.Function("A")(u)
C = sp.Function("C")(u)
B = beta * (u - r1) * (u - r2)
H = A + v * B + w * C
r = (u - r1) / (u - r2)
check_coordinates(
    (u, v, w), {(0, 1): H, (0, 2): 0, (1, 2): 0}, (r, H, w),
    {(0, 1): beta * (r1 - r2) * r * H, (0, 2): 0, (1, 2): 0},
)

Q = kappa * (v * w + 1)
R = sp.Function("R")(v, w)
F = u * Q + R
check_coordinates(
    (u, v, w), {(0, 1): sp.diff(F, w), (0, 2): -sp.diff(F, v), (1, 2): Q},
    (v, v * w + 1, F),
    {(0, 1): kappa * v * (v * w + 1), (0, 2): 0, (1, 2): 0},
)

aa, bb, cc, dd = (sp.Function(name)(v, w) for name in ("a", "b", "c", "d"))
F, G = u * aa + bb, u * cc + dd
alpha = tuple(sp.expand(G * sp.diff(F, x) - F * sp.diff(G, x)) for x in (u, v, w))
check_coordinates(
    (u, v, w), {(0, 1): alpha[2], (0, 2): -alpha[1], (1, 2): alpha[0]},
    (F / G, v, w), {(0, 1): 0, (0, 2): 0, (1, 2): aa * dd - bb * cc},
)

casimir = z**2 / (v * w + 1)
check_coordinates(
    (z, v, w), {(0, 1): -kappa * z * v, (0, 2): kappa * z * w,
                (1, 2): 2 * kappa * (v * w + 1)},
    (z, v, casimir), {(0, 1): -kappa * z * v, (0, 2): 0, (1, 2): 0},
)

check_coordinates(
    (u, v, w), {(0, 1): mu * u * v, (0, 2): -mu * u * w,
                (1, 2): lam * (v * w + 1)},
    (u, v, v * w + 1), {(0, 1): mu * u * v, (0, 2): 0,
                        (1, 2): lam * v * (v * w + 1)},
)

check_coordinates(
    (z, v, w), {(0, 1): -(a + b) * z * v, (0, 2): -b * z * w,
                (1, 2): a * v * w},
    (z / w, v / w, w), {(0, 1): 0, (0, 2): -b * z, (1, 2): a * v},
)

g0, g1, g2, hbar = sp.symbols("g0 g1 g2 hbar")
g = g2 * u**2 + g1 * u + g0
Q = v * w + g
brackets = {(0, 1): mu * u * v, (0, 2): -mu * u * w,
            (1, 2): lam * Q + mu * u * sp.diff(g, u)}
check_coordinates(
    (u, v, w), brackets, (u, v, Q),
    {(0, 1): mu * u * v, (0, 2): 0, (1, 2): lam * v * Q},
)
w_one = w + (g - 1) / v
check_coordinates(
    (u, v, w), brackets, (u, v, w_one),
    {(0, 1): mu * u * v, (0, 2): -mu * u * w_one,
     (1, 2): lam * (v * w_one + 1)},
)

p, q = sp.symbols("p q", nonzero=True)


def clean(poly):
    return {m: sp.factor(c) for m, c in poly.items() if sp.factor(c) != 0}


def add(left, right):
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
    return clean(result)


def scale(coefficient, poly):
    return clean({m: coefficient * c for m, c in poly.items()})


def multiply(left, right):
    """Ordered basis U^a Omega^b V^c, with VU=p^-1 UV, V Omega=q Omega V."""
    result = {}
    for (i, j, k), coefficient in left.items():
        for (ii, jj, kk), second in right.items():
            monomial = i + ii, j + jj, k + kk
            multiplier = p ** (-k * ii) * q ** (k * jj)
            result[monomial] = result.get(monomial, 0) + coefficient * second * multiplier
    return clean(result)


one = {(0, 0, 0): 1}
U, Omega, V, Vinv = ({m: 1} for m in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)))
g_quantum = {(2, 0, 0): g2, (1, 0, 0): g1, (0, 0, 0): g0}
sigma_g = {(i, j, k): coefficient * p ** (-i) for (i, j, k), coefficient in g_quantum.items()}
Fg = add(scale(q, g_quantum), scale(-1, sigma_g))
W = multiply(add(Omega, scale(-1, g_quantum)), Vinv)
W_one = multiply(add(Omega, scale(-1, one)), Vinv)

assert not add(multiply(U, V), scale(-p, multiply(V, U)))
assert not add(multiply(U, W), scale(-p**-1, multiply(W, U)))
assert not add(add(multiply(V, W), scale(-q, multiply(W, V))), scale(-1, Fg))
assert not add(add(multiply(W, V), g_quantum), scale(-1, Omega))
assert not add(multiply(V, Omega), scale(-q, multiply(Omega, V)))
shifted = add(W_one, multiply(add(one, scale(-1, g_quantum)), Vinv))
assert not add(W, scale(-1, shifted))

f_parameter = q * g - g.subs(u, u / p)
first_order = sp.diff(f_parameter.subs({p: 1 + hbar * mu, q: 1 + hbar * lam}), hbar).subs(hbar, 0)
assert sp.simplify(first_order - lam * g - mu * u * sp.diff(g, u)) == 0

x, t, y = sp.symbols("x t y")
f = sp.Function("f")(x)
ric = sp.Function("h")(x, t)
ric_brackets = {(0, 1): 0, (0, 2): f, (1, 2): ric}
assert poisson_bracket(x, y / f, (x, t, y), ric_brackets) == 1
jacobi = sum(
    poisson_bracket((x, t, y)[i],
                    poisson_bracket((x, t, y)[j], (x, t, y)[k], (x, t, y), ric_brackets),
                    (x, t, y), ric_brackets)
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1))
)
assert sp.simplify(jacobi) == 0

print("All seven toric reductions, generic log(1,1,2) link, exact quantum relations,")
print("quantum birational shift, and Riccati Poisson identities passed.")
