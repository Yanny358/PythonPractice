Phone = input("Phone: ")

dicts = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""

for x in Phone:
    output += dicts.get(x) + " "
print(output)
