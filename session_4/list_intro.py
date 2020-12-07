list = ["cơm", "rau"] # container data type
# cơm = index 0
# rau = index 1
print(list)

# C R U D

# Create
list.append("bun cha") 
list.append("bun dau")
list.append("pate")
print(list)

# Read
# Read one
print(list[2])
print(list[3])
print(len(list))

# Assign
first_item = list[0]

# Read all
for i in range(len(list)): # Read All
    print(f'{i}.{list[i]}')

# Update
list[0] = "Phở"
list[3] = "Pizza"
print(list)

# Delete
list.pop(1)
print(list)
deleted_item = list.pop(2)
print(deleted_item)
print(list)

# find index by value
print(list.index("pate"))
item_index

# check a value exists in list
print("bún đậu" in list)
print("Phở" in list)

# Chạy câu điều kiện
if "Phở" in list:
    print(list.index("thịt"))
if "bún đậu" in list:
    print(list.index("bún đậu"))
