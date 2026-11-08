"""Exact checks for the classical blow-up sections of the main manuscript. Python 3 and SymPy."""
import itertools
import sympy as sp

x, y, z = sp.symbols("x y z")
variables = (x, y, z)

def check_zero(expression):
    assert sp.cancel(sp.expand(expression)) == 0

def bracket(f, g, alpha):
    df = [sp.diff(f, v) for v in variables]
    dg = [sp.diff(g, v) for v in variables]
    return (
        alpha[0] * (df[1] * dg[2] - df[2] * dg[1])
        + alpha[1] * (df[2] * dg[0] - df[0] * dg[2])
        + alpha[2] * (df[0] * dg[1] - df[1] * dg[0])
    )

def verify_pencil(s, t, expected, multiplier=1):
    alpha = [multiplier * (s * sp.diff(t, v) - t * sp.diff(s, v))
             for v in variables]
    new_x = t / s
    check_zero(bracket(new_x, y, alpha))
    check_zero(bracket(new_x, z, alpha))
    check_zero(bracket(y, z, alpha) - multiplier * expected)
    recovered_x = (t - x * sp.diff(t, x) - new_x * (s - x * sp.diff(s, x))) / (
        new_x * sp.diff(s, x) - sp.diff(t, x)
    )
    check_zero(recovered_x - x)

# Formal coefficient functions cover every relevant surface line bundle.
a, b, c, d = [sp.Function(name)(y, z) for name in "abcd"]
verify_pencil(x * a + b, x * c + d, b * c - a * d)
print("Fractional-linear pencil transformation verified with arbitrary coefficients.")

# Quadric pencil: entries linear and quadratic in the plane coordinates.
l0, l1 = y, z
r0 = y**2 + 2 * y * z + 3 * z**2 + 5 * y + 7 * z + 11
r1 = 2 * y**2 + 3 * y * z + 5 * z**2 + 7 * y + 11 * z + 13
q0, q1 = x * l0 + r0, x * l1 + r1
cubic = l1 * r0 - l0 * r1
verify_pencil(q0, q1, cubic)
print("Quadric-pencil projection verified.")

# The logarithmic transformation is checked with arbitrary linear functions of z.
coeff = sp.symbols("a0:8")
aa = coeff[0] + coeff[1] * z
bb = coeff[2] + coeff[3] * z
cc = coeff[4] + coeff[5] * z
dd = coeff[6] + coeff[7] * z
f, g = x * aa + bb, x * cc + dd
delta = aa * dd - bb * cc
lam, mu = sp.symbols("lam mu")
alpha = [
    mu * y * (g * sp.diff(f, x) - f * sp.diff(g, x)),
    lam * f * g,
    mu * y * (g * sp.diff(f, z) - f * sp.diff(g, z)),
]
new_x = f / g
check_zero(bracket(new_x, y, alpha))
check_zero(bracket(y, z, alpha) - mu * y * delta)
check_zero(bracket(z, new_x, alpha) - lam * new_x * delta)
print("Logarithmic-to-toric transformation verified.")

# Determinant derivative at a,b,c,d=1,y,z,yz is surjective onto H^0(O(2,2)).
basis11 = [1, y, z, y * z]
columns = []
for h in basis11:
    for k in basis11:
        poly = sp.Poly(h * k, y, z)
        columns.append([poly.coeff_monomial(y**i * z**j)
                        for i, j in itertools.product(range(3), repeat=2)])
assert sp.Matrix.hstack(*map(sp.Matrix, columns)).rank() == 9
print("Dominance of the determinant construction verified.")

# Twenty-four smooth cones of the common permutohedral refinement.
e = [sp.eye(3)[:, i] for i in range(3)]
rays = [-sum(e, sp.zeros(3, 1))] + e
permutohedral = []
for order in itertools.permutations(range(4)):
    cone_rays = [sum((rays[i] for i in order[:k]), sp.zeros(3, 1))
                 for k in (1, 2, 3)]
    matrix = sp.Matrix.hstack(*cone_rays)
    assert abs(matrix.det()) == 1
    permutohedral.append(matrix)

p3 = [sp.Matrix.hstack(*(rays[i] for i in indices))
      for indices in itertools.combinations(range(4), 3)]
cube = [sp.Matrix.hstack(*(signs[i] * e[i] for i in range(3)))
        for signs in itertools.product((-1, 1), repeat=3)]
plane_rays = [e[0], e[1], -e[0] - e[1]]
p1p2 = [sp.Matrix.hstack(sign * e[2], plane_rays[i], plane_rays[j])
        for sign in (-1, 1) for i, j in itertools.combinations(range(3), 2)]

for label, fan in [("P3", p3), ("P1 x P2", p1p2), ("(P1)^3", cube)]:
    inverses = [cone.inv() for cone in fan]
    for cone in permutohedral:
        assert any(all(entry >= 0 for entry in inverse * cone)
                   for inverse in inverses)
    print("All 24 smooth cones refine", label)


def fan_key(cones):
    """Represent a simplicial fan by unordered primitive ray triples."""
    return frozenset(
        frozenset(tuple(int(entry) for entry in cone[:, j]) for j in range(3))
        for cone in cones
    )


def check_smooth_order_fan(fan):
    for cone in fan:
        generators = [sp.Matrix(ray) for ray in cone]
        assert abs(sp.Matrix.hstack(*generators).det()) == 1
        for first, second in itertools.combinations(generators, 2):
            nonzero = [entry for entry in first.cross(second) if entry]
            # Every facet lies in xi_i=0 or xi_i=xi_j.
            assert len(nonzero) == 1 or (
                len(nonzero) == 2 and sum(nonzero) == 0
            )


def star_subdivision(fan, centre):
    centre = frozenset(centre)
    assert len(centre) in (2, 3)
    assert any(centre <= cone for cone in fan)
    new_ray = tuple(sum(entries) for entries in zip(*centre))
    assert all(new_ray not in cone for cone in fan)
    refined = set()
    for cone in fan:
        if centre <= cone:
            refined.update((cone - {ray}) | {new_ray} for ray in centre)
        else:
            refined.add(cone)
    refined = frozenset(refined)
    assert len(refined) == len(fan) + 2
    check_smooth_order_fan(refined)
    return refined


# Explicit blow-up centres in Proposition prop:toric-explicit-blowups.
lattice_basis = tuple(tuple(int(entry) for entry in ray) for ray in e)
e1, e2, e3 = lattice_basis
negative_basis = tuple(tuple(-entry for entry in ray) for ray in lattice_basis)
c_ray, w_ray = (-1, -1, 0), (-1, -1, -1)
p3_rays = tuple(tuple(int(entry) for entry in ray) for ray in rays)
p3_centres = list(itertools.combinations(p3_rays, 3)) + list(
    itertools.combinations(p3_rays, 2)
)
cube_centres = [lattice_basis, negative_basis]
cube_centres += list(itertools.combinations(lattice_basis, 2))
cube_centres += list(itertools.combinations(negative_basis, 2))
p1p2_centres = [
    (e1, e2, e3),
    (c_ray, negative_basis[2]),
    (c_ray, e2),
    (w_ray, e2),
    (c_ray, e1),
    (w_ray, e1),
    (e2, e3),
    (e1, e3),
    (e1, e2),
]
target_fan = fan_key(permutohedral)
assert len(target_fan) == 24
for label, initial, centres in [
    ("P3", p3, p3_centres),
    ("(P1)^3", cube, cube_centres),
    ("P1 x P2", p1p2, p1p2_centres),
]:
    current_fan = fan_key(initial)
    check_smooth_order_fan(current_fan)
    for centre in centres:
        current_fan = star_subdivision(current_fan, centre)
    assert current_fan == target_fan
    print(label, "blow-up sequence of length", len(centres),
          "gives exactly the 24 permutohedral cones.")

# A point centre in dimension three imposes a condition on the first jet.
jet_coefficients = sp.symbols("jet0:9")
jet_matrix = sp.Matrix(3, 3, jet_coefficients)
linear_alpha = jet_matrix * sp.Matrix(variables)
obstruction = sp.Poly((sp.Matrix(variables).T * linear_alpha)[0], *variables)
coefficient_map = sp.Matrix([
    [sp.diff(coefficient, parameter) for parameter in jet_coefficients]
    for coefficient in obstruction.coeffs()
])
assert coefficient_map.rank() == 6
velocity = sp.Matrix(sp.symbols("velocity0:3"))
radial_alpha = sp.Matrix(variables).cross(velocity)
check_zero((sp.Matrix(variables).T * radial_alpha)[0])
for first, second in ((x, y / x), (x, z / x), (y / x, z / x)):
    transformed = sp.cancel(bracket(first, second, radial_alpha))
    chart_x, chart_u, chart_v = sp.symbols("chart_x chart_u chart_v")
    transformed = sp.cancel(transformed.subs(
        {x: chart_x, y: chart_x * chart_u, z: chart_x * chart_v}, simultaneous=True
    ))
    assert not sp.denom(transformed).has(chart_x)
check_zero(bracket(y / x, z / x, [x, 0, 0]) - 1 / x)
print("Point blow-up first-jet criterion and the vanishing-point counterexample verified.")

print("All checks passed.")
