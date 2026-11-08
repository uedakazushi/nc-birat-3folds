"""Exact Jacobian ranks for Poisson bivectors on (P^1)^3. Python 3, no packages."""
from fractions import Fraction
from itertools import product

# w_i is the cyclic coefficient of d_j /\ d_k, equivalently of dx_i
# after contraction with the local volume form dx dy dz.
edges = [(1, 2), (2, 0), (0, 1)]
monomials = [(i, a, b) for i in range(3) for a, b in product(range(3), repeat=2)]
points = list(product(range(3), repeat=3))

def evaluate(coeff, point):
    w, deriv = [0]*3, [[0]*3 for _ in range(3)]
    for (i, a, b), c in zip(monomials, coeff):
        j, k = edges[i]
        x, y = point[j], point[k]
        w[i] += c*x**a*y**b
        if a:
            deriv[i][j] += c*a*x**(a-1)*y**b
        if b:
            deriv[i][k] += c*b*x**a*y**(b-1)
    return w, [deriv[k][j]-deriv[j][k] for j, k in edges]

def rank(rows):
    mat = [list(map(Fraction, row)) for row in rows]
    r = 0
    for j in range(len(mat[0])):
        k = next((i for i in range(r, len(mat)) if mat[i][j]), None)
        if k is None:
            continue
        mat[r], mat[k] = mat[k], mat[r]
        for i in range(r+1, len(mat)):
            t = mat[i][j]/mat[r][j]
            if t:
                mat[i] = [a-t*b for a,b in zip(mat[i], mat[r])]
        r += 1
    return r

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def jacobian_rank(coeff):
    rows = []
    for point in points:
        w, curl = evaluate(coeff, point)
        assert dot(w,curl) == 0
        row = []
        for col in range(27):
            e = [int(j == col) for j in range(27)]
            v, dv = evaluate(e, point)
            row.append(dot(v,curl)+dot(w,dv))
        rows.append(row)
    return rank(rows)

def orbit_rank(coeff):
    # Lie derivative by x_t^d times the coordinate vector field.
    rows = []
    for t, d in product(range(3), repeat=2):
        v = dict.fromkeys(monomials, 0)
        for (i, a, b), c in zip(monomials, coeff):
            j, k = edges[i]
            if t == j and a != d:
                v[i, a+d-1, b] += c*(a-d)
            if t == k and b != d:
                v[i, a, b+d-1] += c*(b-d)
        rows.append([v[m] for m in monomials])
    return rank(rows)

def pencil():
    powers = list(product(range(2), repeat=3))
    f = [2, -1, 4, 2, -3, 5, 1, 3]
    g = [1, 3, -3, 4, 1, 2, -5, -1]
    coeff = {m: 0 for m in monomials}
    for u, fu in zip(powers,f):
        for v, gv in zip(powers,g):
            for i, (j,k) in enumerate(edges):
                if u[i] != v[i]:
                    coeff[i,u[j]+v[j],u[k]+v[k]] += fu*gv*(v[i]-u[i])
    return [coeff[m] for m in monomials]

single_edge = [0,1,3,-1,1,5,5,0,2]+[0]*18
toric = {(0,1,1):1, (1,1,1):3, (2,1,1):5}
axial = {(0,1,1):2, (1,0,2):3, (1,1,1):5, (1,2,0):7, (2,1,1):-2}
if __name__ == '__main__':
    for label, coeff, expected in [('pencil',pencil(),14), ('single edge',single_edge,18),
            ('toric',[toric.get(m,0) for m in monomials],18),
            ('axial',[axial.get(m,0) for m in monomials],17)]:
        actual = jacobian_rank(coeff)
        print(label, 'Jacobian rank', actual, 'affine tangent dimension', 27-actual)
        assert actual == expected
        orbit = orbit_rank(coeff)
        assert orbit == {'pencil':9, 'single edge':6, 'toric':6, 'axial':7}[label]
        print('  orbit dimension', orbit)
