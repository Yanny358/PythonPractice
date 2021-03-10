# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = map(int, input().split())
B = map(int, input().split())

print(*product(A, B))  # about * https://www.python.org/dev/peps/pep-0448/
