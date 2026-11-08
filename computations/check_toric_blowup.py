"""Exact checks for torus cocycle twists and monomial Rees charts.

All coefficients are Laurent monomials in independent q12, q13, q23.
Their exponent vectors are stored exactly.  The general identities are
proved in the manuscript.  These finite checks guard sign and order choices.
"""

from itertools import combinations, permutations, product


ZERO = (0, 0, 0)
STANDARD_BASIS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def negate(vector):
    return tuple(-a for a in vector)


def subtract(left, right):
    return add(left, negate(right))


def cocycle_exponents(left, right):
    return (
        left[0] * right[1],
        left[0] * right[2],
        left[1] * right[2],
    )


def exchange_exponents(left, right):
    return subtract(
        cocycle_exponents(left, right),
        cocycle_exponents(right, left),
    )


def multiply(left, right):
    left_coefficient, left_weight = left
    right_coefficient, right_weight = right
    coefficient = add(
        add(left_coefficient, right_coefficient),
        cocycle_exponents(left_weight, right_weight),
    )
    return coefficient, add(left_weight, right_weight)


def inverse(monomial):
    coefficient, weight = monomial
    inverse_weight = negate(weight)
    inverse_coefficient = negate(
        add(coefficient, cocycle_exponents(weight, inverse_weight))
    )
    result = inverse_coefficient, inverse_weight
    assert multiply(monomial, result) == (ZERO, ZERO)
    assert multiply(result, monomial) == (ZERO, ZERO)
    return result


def determinant(columns):
    a, b, c = columns
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - b[0] * (a[1] * c[2] - a[2] * c[1])
        + c[0] * (a[1] * b[2] - a[2] * b[1])
    )


def check_cocycle_and_homogeneous_maps():
    weights = tuple(product((-1, 0, 1), repeat=3))
    checked = 0
    for m, n, ell in product(weights, repeat=3):
        # Associativity of the algebra product.
        assert add(cocycle_exponents(m, n), cocycle_exponents(add(m, n), ell)) == add(
            cocycle_exponents(n, ell), cocycle_exponents(m, add(n, ell))
        )
        # Right-linearity of f^c(p_ell) = c(m, ell) f(p_ell).
        assert add(cocycle_exponents(ell, n), cocycle_exponents(m, add(ell, n))) == add(
            cocycle_exponents(m, ell), cocycle_exponents(add(ell, m), n)
        )
        # Composition order is c(n, m), when f has weight m and g weight n.
        assert add(cocycle_exponents(m, ell), cocycle_exponents(n, add(ell, m))) == add(
            cocycle_exponents(n, m), cocycle_exponents(add(m, n), ell)
        )
        # The character shift isomorphism is multiplication by c(s, ell).
        s = m
        assert add(
            cocycle_exponents(subtract(ell, s), n),
            cocycle_exponents(s, add(ell, n)),
        ) == add(cocycle_exponents(s, ell), cocycle_exponents(ell, n))
        checked += 1
    print(f"Cocycle, right-linearity, composition and character shifts: {checked} triples.")


def check_rees_charts():
    chart_count = 0
    for ordering in permutations(STANDARD_BASIS):
        coordinates = tuple((ZERO, weight) for weight in ordering)
        for codimension in (2, 3):
            for selected in range(codimension):
                generators = []
                for index, coordinate in enumerate(coordinates):
                    if index < codimension and index != selected:
                        ratio = multiply(coordinate, inverse(coordinates[selected]))
                        assert multiply(ratio, coordinates[selected]) == coordinate
                        generators.append(ratio)
                    else:
                        generators.append(coordinate)
                assert abs(determinant(tuple(item[1] for item in generators))) == 1
                for left, right in combinations(generators, 2):
                    forward = multiply(left, right)
                    backward = multiply(right, left)
                    assert forward[1] == backward[1]
                    assert subtract(forward[0], backward[0]) == exchange_exponents(
                        left[1], right[1]
                    )
                chart_count += 1

    e1, e2, e3 = STANDARD_BASIS
    assert exchange_exponents(subtract(e2, e1), subtract(e3, e1)) == (1, -1, 1)
    assert exchange_exponents(subtract(e2, e1), e3) == (0, -1, 1)
    print(f"Point and curve Rees charts: {chart_count} unimodular charts.")
    print("Point chart exchange q(u,v) = q12*q23/q13.")
    print("Curve chart exchange q(u,x3) = q23/q13.")


def check_exceptional_lengths():
    counts = {
        "P3": (4, 4, 6),
        "P1xP2": (6, 1, 8),
        "P1xP1xP1": (8, 2, 6),
    }
    for name, (initial, points, curves) in counts.items():
        length = initial + 2 * points + 2 * curves
        assert length == 24
        print(f"{name}: {initial} + 2*{points} + 2*{curves} = {length}.")


if __name__ == "__main__":
    check_cocycle_and_homogeneous_maps()
    check_rees_charts()
    check_exceptional_lengths()
