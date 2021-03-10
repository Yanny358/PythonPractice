"""Print  lines where each line  (in the range 1 <= i <= n) contains the respective
decimal, octal, capitalized hexadecimal, and binary values of i.
Each printed value must be formatted to the width of the binary value of n."""


def print_formatted(number):
    for i in range(1, number + 1):
        width = len(f"{number:b}")
        print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")


if __name__ == '__main__':
    print("Enter number")
    n = int(input())
    print_formatted(n)
