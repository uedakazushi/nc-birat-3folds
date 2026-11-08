#!/usr/bin/env python3
"""Exact checks of semiclassical identities, using SymPy 1.14.0.

These checks supplement the proofs in poisson_quantization.tex. They do not
prove AS regularity, global formality, or Artin approximation.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product

import sympy as sp


def check_toric_cocycle():
    m = sp.symbols("m0:3")
    n = sp.symbols("n0:3")
    p = sp.symbols("p0:3")
    for i in range(3):
        for j in range(i + 1, 3):
            difference = (
                m[i] * n[j]
                + (m[i] + n[i]) * p[j]
                - n[i] * p[j]
                - m[i] * (n[j] + p[j])
            )
            assert sp.expand(difference) == 0
    print("Toric bicharacter associativity verified symbolically.")


def check_plane_normalization():
    x = sp.symbols("X0:3")
    monomials = [
        sp.prod(x[i] ** exponents[i] for i in range(3))
        for exponents in product(range(4), repeat=3)
        if sum(exponents) == 3
    ]
    coefficients = sp.symbols(f"c0:{len(monomials)}")
    cubic = sum(c * monomial for c, monomial in zip(coefficients, monomials))
    bracket_matrix = sp.Matrix(
        [
            [0, sp.diff(cubic, x[2]), -sp.diff(cubic, x[1])],
            [-sp.diff(cubic, x[2]), 0, sp.diff(cubic, x[0])],
            [sp.diff(cubic, x[1]), -sp.diff(cubic, x[0]), 0],
        ]
    ) / 3
    u = x[1] / x[0]
    v = x[2] / x[0]
    du = sp.Matrix([sp.diff(u, xi) for xi in x])
    dv = sp.Matrix([sp.diff(v, xi) for xi in x])
    assert sp.simplify((du.T * bracket_matrix * dv)[0] - cubic / x[0] ** 3) == 0
    print("The factor 1/3 gives the prescribed projective cubic bracket.")


def rotate_twice(tensor):
    return {word[2:] + word[:2]: coefficient for word, coefficient in tensor.items()}


def symmetric_pair(power):
    return {
        0: [((0, 0), Fraction(1))],
        1: [((0, 1), Fraction(1, 2)), ((1, 0), Fraction(1, 2))],
        2: [((1, 1), Fraction(1))],
    }[power]


def check_quadric_tensor():
    w0 = {
        (0, 0, 1, 1): Fraction(1),
        (1, 0, 0, 1): Fraction(-1),
        (0, 1, 1, 0): Fraction(-1),
        (1, 1, 0, 0): Fraction(1),
    }
    assert rotate_twice(w0) == w0
    for a_power, b_power in product(range(3), repeat=2):
        tensor = {}
        for (a_left, a_right), a_coefficient in symmetric_pair(a_power):
            for (b_left, b_right), b_coefficient in symmetric_pair(b_power):
                tensor[(a_left, b_left, a_right, b_right)] = a_coefficient * b_coefficient
        assert rotate_twice(tensor) == tensor

    # Contract the last B factor with b_0^* and set the a_0,b_0 arrows to 1.
    # The remaining relation must be uv - vu - t for D=a_0^2 b_0^2.
    t = sp.Symbol("t")
    highest_weight_tensor = dict(w0)
    highest_weight_tensor[(0, 0, 0, 0)] = -t
    reduced = defaultdict(lambda: 0)
    for word, coefficient in highest_weight_tensor.items():
        if word[3] == 0:
            local_word = tuple(
                ("u" if position % 2 == 0 else "v")
                for position, index in enumerate(word[:3])
                if index == 1
            )
            reduced[local_word] += coefficient
    assert dict(reduced) == {("v", "u"): -1, ("u", "v"): 1, (): -t}
    print("Quadric two-periodicity and the highest-weight normalization verified.")


def check_logarithmic_equivariance():
    x, z, a, b, c = sp.symbols("x z a b c")
    quadratic = a * x**2 + b * x * z + c * z**2
    assert sp.expand(x * sp.diff(quadratic, x) + z * sp.diff(quadratic, z) - 2 * quadratic) == 0
    t, kappa = sp.symbols("t kappa")
    for weight in range(-3, 4):
        assert sp.diff((1 + t * kappa) ** weight, t).subs(t, 0) == weight * kappa
    print("Radial invariance and the Ore mixed semiclassical term verified.")


if __name__ == "__main__":
    check_toric_cocycle()
    check_plane_normalization()
    check_quadric_tensor()
    check_logarithmic_equivariance()
    print("All quantization identity checks passed.")
