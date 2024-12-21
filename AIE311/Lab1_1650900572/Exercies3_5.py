print("__________________________________Exercise 3: Create 1D array String___________________________________")
array_id = ["Number ID", "Name", "Count"]

length_of_array = len(array_id)
print("Length of Array:", length_of_array)

index_of_name = array_id.index("Name")
print("Index of 'Name' in Array:", index_of_name)

array_id.append("Status")
print("Array after adding 'Status':\n", array_id)


print("__________________________________Exercise 4: Create 2D array___________________________________")

matrix_2d = [["Number ID", "Name", "Count", "Status"], []]

matrix_2d = list(matrix_2d)

length_of_matrix = len(matrix_2d)
print("Length of Matrix:", length_of_matrix)

matrix_2d.append([1, "Rubber", 0, "Out of stock"])
matrix_2d.append([2, "Ruler", 5, "In stock"])
matrix_2d.append([3, "Pencil", 1, "In stock"])

for row in matrix_2d:
    print(row)

print("__________________________________Exercise 5: Create 2D array continue___________________________________")

matrix_2d = [
    ["Number ID", "Name", "Count", "Status"],
    [],
    [1, "Rubber", 0, "Out of stock"],
    [2, "Ruler", 5, "In stock"],
    [3, "Pencil", 1, "In stock"]
]

matrix_2d.append([4, "Pen", 10, "In stock"])
matrix_2d.append([5, "Colour pencil", 5, "In stock"])
matrix_2d.append([6, "A4 Paper", 0, "Out of stock"])


print("\nItems In Stock:")
for item in matrix_2d[2:]:
    if item and item[3] == "In stock":
        print(item)

print("\nItems Out of Stock:")
for item in matrix_2d[2:]:
    if item and item[3] == "Out of stock":
        print(item)
# Buyer
Ruler = 1
Pencil = 1
Pen  =  2
Colour_pencil = 1

for item in matrix_2d[2:]:
    if item and item[1] == "Ruler":
        item[2] -= Ruler
    elif item and item[1] == "Pencil":
        item[2] -= Pencil
    elif item and item[1] == "Pen":
        item[2] -= Pen
    elif item and item[1] == "Colour pencil":
        item[2] -= Colour_pencil

for item in matrix_2d[2:]:
    if item and item[2] == 0:
        item[3] = "Out of stock"
    elif item:
        item[3] = "In stock"

print("\nRemaining Items:")
for row in matrix_2d:
    print(row)
