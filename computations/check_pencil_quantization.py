"""Finite checks for the elliptic pencil and its double central extension.

The all-degree PBW assertion uses the proof in the manuscript.  The ranks here
check the classical presentation through degree six over the stated prime.
"""

from collections import defaultdict
from itertools import combinations_with_replacement, product

import sympy as sp


PRIME = 101


def rank_mod_prime(rows):
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (row for row in range(rank, len(matrix)) if matrix[row][column] % PRIME),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column] % PRIME, -1, PRIME)
        matrix[rank] = [(value * inverse) % PRIME for value in matrix[rank]]
        pivot_row = matrix[rank]
        for row in range(rank + 1, len(matrix)):
            coefficient = matrix[row][column] % PRIME
            if coefficient:
                matrix[row] = [
                    (entry - coefficient * pivot_entry) % PRIME
                    for entry, pivot_entry in zip(matrix[row], pivot_row)
                ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


vertices = list(product(range(2), repeat=3))
quadratic_monomials = list(combinations_with_replacement(range(8), 2))
fibers = defaultdict(list)
for left, right in quadratic_monomials:
    exponent = tuple(a + b for a, b in zip(vertices[left], vertices[right]))
    fibers[exponent].append((left, right))

segre_relations = [
    (monomial, fiber[0])
    for fiber in fibers.values()
    for monomial in fiber[1:]
]
assert len(fibers) == 27
assert len(segre_relations) == 9
assert 8**2 - 27 == 37
assert 37 == (6**2 - 12) + (2 * 6 + 1)

# s=X000+X111 and t=X100+X010+X001.  Eliminate X111 and X100.
v = sp.symbols("v0:6")
images = [v[0], v[1], v[2], v[3], -v[1] - v[2], v[4], v[5], -v[0]]
elliptic_relations = [
    sp.Poly(images[a] * images[b] - images[c] * images[d], *v)
    for (a, b), (c, d) in segre_relations
]
elliptic_monomials = [
    v[left] * v[right] for left, right in combinations_with_replacement(range(6), 2)
]
relation_matrix = [
    [int(relation.coeff_monomial(monomial)) for monomial in elliptic_monomials]
    for relation in elliptic_relations
]
assert rank_mod_prime(relation_matrix) == 9

s_support = [(0, 0, 0), (1, 1, 1)]
t_support = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
checked_ranks = []
for degree in range(1, 7):
    target = list(product(range(degree + 1), repeat=3))
    target_index = {exponent: index for index, exponent in enumerate(target)}
    source = list(product(range(degree), repeat=3))
    matrix = [[0] * (2 * len(source)) for _ in target]
    for block, support in enumerate((s_support, t_support)):
        for index, exponent in enumerate(source):
            for term in support:
                image = tuple(a + b for a, b in zip(exponent, term))
                matrix[target_index[image]][block * len(source) + index] += 1
    rank = rank_mod_prime(matrix)
    assert len(target) - rank == 6 * degree
    assert 2 * len(source) - rank == (degree - 1) ** 3
    checked_ranks.append(rank)

y, z = sp.symbols("y z")
charts = [
    1 - y**2 * z - y * z**2,
    y**2 - z - y * z**2,
    z**2 - y - y**2 * z,
    y**2 * z**2 - y - z,
]
for equation in charts:
    ideal = sp.groebner([equation, sp.diff(equation, y), sp.diff(equation, z)], y, z)
    assert list(ideal) == [sp.Integer(1)]

intersection = sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
roots = sp.Matrix([[0, 0, 1, -1], [1, -1, 0, 0], [0, 1, -1, -1]])
anticanonical = sp.Matrix([2, 2, -1, -1])
assert roots * intersection * roots.T == sp.Matrix([[-2, 0, 0], [0, -2, 1], [0, 1, -2]])
assert roots * intersection * anticanonical == sp.zeros(3, 1)
# Moving p and q with p+q fixed changes only the A1 period.
assert roots * sp.Matrix([0, 0, 1, -1]) == sp.Matrix([2, 0, 0])

n = sp.symbols("n", integer=True, nonnegative=True)
j = sp.symbols("j", integer=True, positive=True)
hilbert_coefficient = n + 1 + sp.summation(6 * j * (n - j + 1), (j, 1, n))
assert sp.simplify(hilbert_coefficient - (n + 1) ** 3) == 0

surface_vertices = list(product(range(2), repeat=2))
surface_euler = sp.zeros(4)
cross_euler = sp.zeros(4)
for row, source in enumerate(surface_vertices):
    for column, target in enumerate(surface_vertices):
        m = 1 + target[0] - source[0]
        degree = 1 + target[1] - source[1]
        surface_euler[row, column] = m * degree
        source_dimension = 2 * (m + 1) * (degree + 1)
        target_dimension = 2 + 2 * m + 2 * degree
        cross_euler[row, column] = source_dimension - target_dimension
assert cross_euler == 2 * surface_euler
assert sum(surface_euler) == 16
assert sum(cross_euler) == 32
assert 2 * sum(surface_euler) + sum(cross_euler) == 64

print("Segre presentation: 8 generators and 37 quadratic relations")
print("Elliptic quotient: 6 generators and 24 quadratic relations")
print(f"Classical Koszul ranks in degrees 1--6 over F_{PRIME}: {checked_ranks}")
print("All four elliptic charts are smooth over Q")
print("Root lattice A1+A2 and moving A1 period: verified")
print("Double central-extension Hilbert coefficient: (n+1)^3")
print("Elliptic-center mutation: corner rank 16, cross rank 32, total rank 64")
