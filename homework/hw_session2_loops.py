# Session 2: Conditional and Loops 
# Loops

# Exercise 1
sum = 0
x = int(input("Số số hạng: "))
for i in range(x + 1):
    sum = sum + i
print("Tổng các số là: ", sum)

# Exercise 2
sum = 0
x = int(input("Số số hạng: "))
for i in range(x + 1):
    sum = sum + (i * 2 + 1)
print("Tổng S là: ", sum)

# Exercise 3
sum = 0
x = int(input("Số số hạng: "))
for i in range(1, x + 1):
    sum = sum + (i * 2)
print("Tổng S là: ", sum)

# Exercise 4
sum = 0
x = int(input("Nhập số N: "))
for i in range(1, x):
    sum = sum + (1 / i)
print("Tổng S là: ", sum)

# Exercise 5
sum = 0
x = int(input("Nhập số N: "))
for i in range(1, x):
    sum = sum + (1 / (i * (i + 1)))
print("Tổng S là: ", sum)

# Exercise 7
width = int(input("Nhập chiều rộng: "))
length = int(input("Nhập chiều dài: "))
for a in range(1, width + 1):
    print("*" * length)
    print()

# Exercise 8
a = int(input("Số hàng: "))
for i in range(a + 1):
    print("*" * i)
    print()

# Exercise 9
password = str(input("Nhập mật khẩu: "))
while len(password) < 8:
    password = str(input("Nhập lại mật khẩu lớn hơn hoặc bằng 8 kí tự: "))

# Exercise 11:
password = str(input("Nhập mật khẩu: "))
while len(password) < 8: 
    password = str(input("Nhập lại mật khẩu lớn hơn hoặc bằng 8 kí tự: "))
for i in range(1, len(password) + 1):
    if password[i] != "$" or password[i] != "%" or password[i] != "_":
        if i == len(password):
            print("Nhập lại mật khẩu chứa 1 trong 3 kí tự ($, %, _): ")
    else:
        break

# Exercise 12
x = int(input("Nhập số: "))
import math
if type(math.sqrt(x))  int:
    print("Đây là số chính phương.")

