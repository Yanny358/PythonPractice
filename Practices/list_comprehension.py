matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(len(matrix))
transpose = [[row[i] for row in matrix] for i in range(2)]  # for i in range comes first
print(transpose)

# In above program, we have a variable matrix which have 4 rows and 2 columns.

my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
print(my_list)