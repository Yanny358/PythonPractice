length = 10
k = length
for p in range(0, length):
    for n in range(0, k):
        print(end=" ")
    k = k - 1
    for n in range(0, p + 1):
        print("@", end=' ')
    print("")
