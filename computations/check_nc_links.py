"""Exact checks for the birational formulas in noncommutative_birational.tex.

Requires Python 3 and SymPy. Classification and AS regularity use the cited
theorems. These checks cover the displayed algebraic identities.
"""

import sympy as sp


def check_fractional_linear_order():
    """Noncommuting matrices detect the order of the displayed inverses."""
    matrices = [
        sp.Matrix([[1, 2], [0, 1]]),
        sp.Matrix([[0, 1], [1, 1]]),
        sp.Matrix([[2, 0], [1, 1]]),
        sp.Matrix([[1, 1], [2, 3]]),
    ]
    a, b, c, d = matrices
    assert a * c != c * a
    count = 0
    for u in range(2, 12):
        denominator = u * a - c
        if denominator.det() == 0:
            continue
        x = denominator.inv() * (d - u * b)
        if (a * x + b).det() == 0:
            continue
        assert (c * x + d) * (a * x + b).inv() == u * sp.eye(2)
        count += 1
    assert count >= 5


def check_gwa_semiclassical_formula():
    x, z, a, b, c, h = sp.symbols("x z a b c h")
    ly = b * x / 2 + c * z
    lz = -a * x - b * z / 2
    assert sp.expand(z * ly - x * lz) == a * x**2 + b * x * z + c * z**2
    linear_map = sp.Matrix([[b / 2, c], [-a, -b / 2]])
    assert linear_map**2 == (b**2 / 4 - a * c) * sp.eye(2)
    determinant = (sp.eye(2) + h * linear_map).det()
    assert sp.expand(determinant - 1 + h**2 * (b**2 / 4 - a * c)) == 0


def check_quantum_torus_change():
    p, q = sp.symbols("p q", nonzero=True)

    def cocycle(m, n):
        return q ** (-m[1] * n[0]) * p ** (m[2] * (n[0] + n[1]))

    def add(m, n):
        return tuple(a + b for a, b in zip(m, n))

    samples = [(1, -1, 0), (0, 1, 0), (0, 0, 1), (-2, 1, 3)]
    for m in samples:
        for n in samples:
            for ell in samples:
                left = cocycle(m, n) * cocycle(add(m, n), ell)
                right = cocycle(n, ell) * cocycle(m, add(n, ell))
                assert sp.simplify(left / right) == 1
    a, s, y = samples[:3]
    assert sp.simplify(cocycle(y, a) / cocycle(a, y)) == 1
    assert sp.simplify(cocycle(a, s) / cocycle(s, a)) == q
    assert sp.simplify(cocycle(y, s) / cocycle(s, y)) == p


def check_hesse_family():
    x, y, z, b, h, lam = sp.symbols("x y z b h lam")
    matrix = sp.Matrix([[-h * x, b * z, y], [z, -h * y, b * x], [b * y, x, -h * z]])
    cubic = x**3 + y**3 + z**3 - 3 * lam * x * y * z
    base_equation = 1 + b**3 - h**3 + 3 * lam * b * h
    assert sp.expand(matrix.det() - b * h * cubic - x * y * z * base_equation) == 0
    assert sp.diff(base_equation, b).subs({b: -1, h: 0}) == 3
    tangent = -sp.diff(base_equation, h) / sp.diff(base_equation, b)
    assert sp.simplify(tangent.subs({b: -1, h: 0})) == lam
    for n in range(9):
        products = {
            (2 * n - i - j, i, j)
            for i in range(n + 1)
            for j in range(n + 1)
        }
        assert len(products) == (n + 1) ** 2
        assert all(min(monomial) >= 0 for monomial in products)


if __name__ == "__main__":
    check_fractional_linear_order()
    check_gwa_semiclassical_formula()
    check_quantum_torus_change()
    check_hesse_family()
    print("PASS: noncommutative inverse order, GWA bracket, quantum monomials, Hesse family")
