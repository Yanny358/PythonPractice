import string

'''def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    result = ["-".join(alpha[i:size][::-1] + alpha[i:size][1:]).center(width, "-")
              for i in range(size)]
    print("\n".join(result[::-1] + result[1:]))'''


def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    result = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        result.append((s[::-1] + s[1:]).center(width, "-"))
    print('\n'.join(result[::-1] + result[1:]))


if __name__ == '__main__':
    print("Enter number from 2 to 26")
    n = int(input())
    print_rangoli(n)
