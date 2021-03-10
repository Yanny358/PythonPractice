
print("Enter two numbers separated by space(first number must be odd and second number must be 3x first number)")
x, y = map(int, input().split())
pattern = [('.|.' * (2 * i + 1)).center(y, '-') for i in range(x // 2)]
print('\n'.join(pattern + ['WELCOME'.center(y, '-')] + pattern[::-1]))

# ALTERNATIVE
'''x, y = map(int, input().split())
str1 = ".|."
for i in range(1, x, 2):
    print((str1 * i).center(y, "-"))
print("WELCOME".center(y, "-"))
for i in range(x - 2, 0, -2):
    print((str1 * i).center(y, "-"))'''
