# N -> f[i][j] ada N macem
# i,j -> M
n = int(input())
m = int(input())
k = int(input())
variables = {}

for i in range(n):
    a = int(input())
    b = int(input())
    c = int(input())
    variables[i] = [a,b,c]

print(variables)