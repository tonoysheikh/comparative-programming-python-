import re

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_script = ''
for j in range(m):
    for i in range(n):
        decoded_script += matrix[i][j]

decoded_script = re.sub(r'([a-zA-Z0-9])[^a-zA-Z0-9]+([a-zA-Z0-9])', r'\1 \2', decoded_script)
print(decoded_script)