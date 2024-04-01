from pprint import pprint

p = [5, 12, 3, 10, 5, 40]
size = len(p) - 1

# Create and initialize memoization tables for M and S
M: list[list[float]] = []
S: list[list[float]] = []
for x in range(size + 1):
    M.append([])
    S.append([])
    for y in range(size + 1):
        M[-1].append(float("inf"))
        S[-1].append(float("nan"))


def lookup_chain(i: int, j: int):
    if M[i][j] < float("inf"):
        return M[i][j]
    
    if i == j:
        M[i][j] = 0
    else:
        for k in range(i, j):
            q = lookup_chain(i, k) + lookup_chain(k+1, j) + p[i-1]*p[k]*p[j]
            if q < M[i][j]:
                M[i][j] = q
                S[i][j] = k
    return M[i][j]

# S[1][2] = 1
# S[2][3] = 2
# S[3][4] = 3
# S[4][5] = 4

# S[1][3] = 2
# S[2][4] = 2
# S[3][5] = 4

# S[1][4] = 3
# S[2][5] = 3

# S[1][5] = 4

def print_opt_parens(s: list[list[int]], i: int, j: int):
    if i == j:
        print(f" A{i} ", end="")
    else:
        print(f"(", end="")
        print_opt_parens(s, i, s[i][j])
        print_opt_parens(s, s[i][j] + 1, j)
        print(f")", end="")


result = lookup_chain(1, size)

print(f"{p=}")
print()
print(f"M[1,{size}]={result}")
print()
print(f"M matrix:")
pprint(M)
print()
print(f"S matrix:")
pprint(S)
print()
print(f"Final result:")
print_opt_parens(S, 1, size)
