#!/usr/bin/env python3
"""Exact finite checks for the two product Beilinson algebras.

Python 3 standard library only.
This computes corner dimensions, the inverse Hilbert matrix, and dimensions
of relative normalized Hochschild cochain spaces. It does not independently
prove formality, Artin approximation, or Koszulness.
"""

from itertools import combinations, product
from math import comb, prod


def product_beilinson_data(bounds):
    vertices = sorted(
        product(*(range(bound + 1) for bound in bounds)),
        key=lambda vertex: (sum(vertex), vertex),
    )

    def strict_order(first, last):
        return first != last and all(a <= b for a, b in zip(first, last))

    def corner_dimension(first, last):
        if any(a > b for a, b in zip(first, last)):
            return 0
        return prod(
            comb(bound + b - a, bound)
            for bound, a, b in zip(bounds, first, last)
        )

    size = len(vertices)
    hilbert = [
        [corner_dimension(first, last) for last in vertices]
        for first in vertices
    ]
    inverse = [[int(i == j) for j in range(size)] for i in range(size)]
    for gap in range(1, size):
        for i in range(size - gap):
            j = i + gap
            inverse[i][j] = -sum(
                hilbert[i][k] * inverse[k][j] for k in range(i + 1, j + 1)
            )
    assert all(
        sum(hilbert[i][k] * inverse[k][j] for k in range(size)) == int(i == j)
        for i in range(size)
        for j in range(size)
    )

    hilbert_by_degree = []
    tor_by_degree = []
    for degree in range(4):
        positions = [
            (i, j)
            for i, first in enumerate(vertices)
            for j, last in enumerate(vertices)
            if sum(last) - sum(first) == degree
        ]
        hilbert_by_degree.append(sum(hilbert[i][j] for i, j in positions))
        tor_by_degree.append(
            sum((-1) ** degree * inverse[i][j] for i, j in positions)
        )
        assert all(
            (-1) ** degree * inverse[i][j] >= 0 for i, j in positions
        )

    cochain_dimensions = []
    for degree in range(1, 5):
        dimension = 0
        for chain in combinations(vertices, degree + 1):
            adjacent_pairs = list(zip(chain, chain[1:]))
            if all(strict_order(first, last) for first, last in adjacent_pairs):
                dimension += corner_dimension(chain[0], chain[-1]) * prod(
                    corner_dimension(first, last)
                    for first, last in adjacent_pairs
                )
        cochain_dimensions.append(dimension)

    return {
        "rank": sum(hilbert_by_degree),
        "hilbert": hilbert_by_degree,
        "tor": tor_by_degree,
        "cochains_1_to_4": cochain_dimensions,
    }


def main():
    expected = [
        (
            "P1 x P2",
            (1, 2),
            {
                "rank": 60,
                "hilbert": [6, 18, 24, 12],
                "tor": [6, 18, 18, 6],
                "cochains_1_to_4": [336, 972, 648, 0],
            },
        ),
        (
            "(P1)^3",
            (1, 1, 1),
            {
                "rank": 64,
                "hilbert": [8, 24, 24, 8],
                "tor": [8, 24, 24, 8],
                "cochains_1_to_4": [208, 576, 384, 0],
            },
        ),
    ]
    for name, bounds, target in expected:
        actual = product_beilinson_data(bounds)
        assert actual == target, (name, actual)
        print(name, actual)
    print("All corner, Hilbert-inverse, and chain-length checks passed.")


if __name__ == "__main__":
    main()
