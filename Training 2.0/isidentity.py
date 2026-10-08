matrix=[
    [1,0,0],
    [1,0,0],
    [1,0,0]
]

n = len(matrix)
is_identity = True

for i in range(n):
    for j in range(n):

        if i == j:
            if matrix[i][j] != 1:
                is_identity = False
        else:
            if matrix[i][j] != 0:
                is_identity = False

print(is_identity)