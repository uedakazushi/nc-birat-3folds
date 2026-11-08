"""Rank lower bounds for the concurrent-line family. Pure Python 3."""
from itertools import product

MOD = 101

def jacobi_row(t, x, y):
    f = (x - 1) * (x + 2) * (x - 3)
    df = 3*x*x - 4*x - 5
    h = 1 + 2*t + 3*t*t + x*(5 + 7*t + 11*t*t)
    dh = 2 + 6*t + x*(7 + 22*t)
    row = []
    # Each (a, ax, by) represents the data needed from a plane vector (a,b).
    fields = [(1,0,0), (0,0,0), (x,1,0), (y,0,0), (0,0,0),
              (0,0,1), (x*x,2*x,x), (x*y,y,2*y)]
    for k in range(3):
        tk = t**k
        dt = k*t**(k-1) if k else 0
        for a, ax, by in fields:
            row.append(tk*a*(df + dh) - h*dt*a - f*tk*(ax + by))
    for i in range(4):
        for j in range(4-i):
            row.append(h*j*x**i*y**(j-1) if j else 0)
    return row

def rank(rows):
    rows = [[n % MOD for n in row] for row in rows]
    r = 0
    for c in range(len(rows[0])):
        p = next((i for i in range(r,len(rows)) if rows[i][c]), None)
        if p is None:
            continue
        rows[r],rows[p] = rows[p],rows[r]
        inv = pow(rows[r][c], -1, MOD)
        for i in range(r+1,len(rows)):
            factor = rows[i][c]*inv % MOD
            rows[i] = [(x-factor*y) % MOD for x,y in zip(rows[i],rows[r])]
        r += 1
    return r

matrix = [jacobi_row(*point) for point in product(range(3),range(4),range(4))]
fixed = rank([row[:24] for row in matrix])
ambient = rank(matrix)
print('Concurrent triple fixed-cubic and ambient ranks modulo 101:', fixed, ambient)
assert (fixed, ambient) == (18,21)
