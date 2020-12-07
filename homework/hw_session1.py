# Session 1: Variables and data types

# Exercise 1
# Input x
x = float(input("Enter x: "))
import math

# Calculate and output y1 and y2
y1 = (x ** 2 + 10 * x + math.sqrt(x) + 3 * x + 1) * 4
print("y1 = ", y1)

a = math.sin(math.pi * x ** 2) + math.sqrt(x ** 2 + 1)
b = math.e ** (2 * x) + math.cos((math.pi) * x / 4)
y2 = a / b
print("y2 = ", y2)

# Exercise 2
# Input số tiền
y = int(input("Số nghìn đồng: ", ))

# Tính số tờ của từng mệnh giá tiền
a = int(y //100)
b = int(y % 100)
c = int(b // 50)
d = int(b % 50)
e = int(d // 20)
f = int(d % 20)
g = int(f / 10)

# Output kết quả
print("y = ", a, "tờ 100.000", "+", c, "tờ 50.000", "+", e, "tờ 20.000", "+", g, "tờ 10.000") 

# Exercise 3
# Input số có 3 chữ số
x = str(input("Nhập số có 3 chữ số: "))
a = int(x[0])
b = int(x[1])
c = int(x[2])
sum = a + b + c
print("Tổng các chữ số là", sum)
