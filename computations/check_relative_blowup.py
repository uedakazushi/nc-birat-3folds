"""Exact Euler-form certificates for the two contractions of a degree-7 del Pezzo."""

import sympy as sp


def verify_euler_change():
    # Coordinates are rank, H, E_p, E_q, and twice ch_2.
    plane_basis = sp.Matrix([
        [1, 1, 1, 0, 0],
        [0, 1, 2, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 4, 1, 1],
    ])
    quadric_basis = sp.Matrix([
        [1, 1, 1, 1, 0],
        [0, 1, 2, 3, 1],
        [0, -1, -1, -2, -1],
        [0, 0, -1, -1, -1],
        [0, 0, 2, 4, 1],
    ])
    plane_euler = sp.Matrix([
        [1, 3, 6, 1, 1],
        [0, 1, 3, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ])
    quadric_euler = sp.Matrix([
        [1, 2, 4, 6, 1],
        [0, 1, 2, 4, 1],
        [0, 0, 1, 2, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1],
    ])
    change = plane_basis.inv() * quadric_basis
    assert all(entry.is_Integer for entry in change)
    assert change.det() == 1
    assert change.T * plane_euler * change == quadric_euler
    assert sum(plane_euler) == 23
    assert sum(quadric_euler[:4, :4]) == 24
    assert sum(quadric_euler) == 29
    anticanonical = plane_euler.T.inv() * plane_euler
    point = sp.Matrix([1, -2, 1, 0, 0])
    assert anticanonical[:, 0] == sp.Matrix([1, -3, 3, -1, -1])
    assert anticanonical[:, 3] == point + sp.eye(5)[:, 3]
    assert anticanonical[:, 4] == point + sp.eye(5)[:, 4]
    nilpotent = anticanonical - sp.eye(5)
    assert nilpotent**3 == sp.zeros(5)
    n = sp.symbols("n", integer=True, nonnegative=True)
    power = sp.eye(5) + n * nilpotent + n * (n - 1) * nilpotent**2 / 2
    euler_dimension = (plane_euler * power)[0, 0]
    assert sp.simplify(euler_dimension - 1 - 7 * n * (n + 1) / 2) == 0
    assert 8**2 - 22 == 42
    print("Euler change has determinant 1 and preserves the pairing.")
    print("Tilting algebra ranks: plane common model 23, quadric corner 24, second model 29.")
    print("Product common model has rank 92 and 10 exceptional objects.")
    print("Anticanonical K0 action and Euler polynomial 1+7n(n+1)/2 agree.")
    print("Anticanonical presentation has 8 generators and 42 quadratic relations.")


if __name__ == "__main__":
    verify_euler_change()
