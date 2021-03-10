""""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types.
Iterate through each command in order and perform the corresponding operation on your list.
"""

if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        x = input().split()
        command = x[0]
        if command == 'append':
            result.append(int(x[1]))
        if command == 'print':
            print(result)
        if command == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if command == 'reverse':
            result.reverse()
        if command == 'pop':
            result.pop()
        if command == 'sort':
            result.sort()
        if command == 'remove':
            result.remove(int(x[1]))
        # print(result) for printing after each command
