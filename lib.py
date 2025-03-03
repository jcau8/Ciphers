# Function to get cofactor of mat[p][q] in cof[][]
def get_cof(mat, cof, p, q, n):
    i = 0
    j = 0
    for row in range(n):
        for col in range(n):
            if row != p and col != q:
                cof[i][j] = mat[row][col]
                j += 1
                if j == n - 1:
                    j = 0
                    i += 1

# Recursive function for finding determinant
# of matrix mat of dimension n
def get_det(mat, n):
    if n == 1:
        return mat[0][0]
    det = 0
    cof = [[0] * n for _ in range(n)]  # To store cofactors
    sign = 1
    for f in range(n):
        get_cof(mat, cof, 0, f, n)
        det += sign * mat[0][f] * get_det(cof, n - 1)
        sign = -sign
    return det

# Function to get adjoint of mat in adj
def adjoint(mat, adj, mod):
    n = len(mat)
    if n == 1:
        adj[0][0] = 1
        return
    sign = 1
    cof = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            get_cof(mat, cof, i, j, n)
            sign = 1 if (i + j) % 2 == 0 else -1
            adj[j][i] = (sign * get_det(cof, n - 1)) % mod

# Function to calculate and store inverse, returns 
# false if matrix is singular
def inverse(mat, mod):
    n = len(mat)
    det = get_det(mat, n) % mod
    # calculate the multiplicative inverse
    detinv = pow(int(det), -1, mod)
    if det == 0:
        print("Singular matrix, can't find its inverse")
        return None
    adj = [[0] * n for _ in range(n)]
    adjoint(mat, adj, mod)
    # print(f'Adjoint matrix: {adj}')
    inv = [[(adj[i][j] * detinv) % mod for j in range(n)] for i in range(n)]
    return inv