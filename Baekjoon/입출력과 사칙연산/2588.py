# 곱셈

'''
A = int(input())

B = input()

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))
'''

a = int(input())
b = input()

for i in range(len(b)):
  print(a * int(b[len(b) - (i + 1)]))

print(a * int(b))
