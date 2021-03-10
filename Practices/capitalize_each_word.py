def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    print(s)


if __name__ == '__main__':
    s = input()

    solve(s)
