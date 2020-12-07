# Session 2: Conditional and Loops 
# Conditionals
# Exercise 1: Kiểm tra năm có bao nhiêu ngày
x = int(input("Năm bao nhiêu? "))
if x % 4 == 0:
    print("Đây là năm nhuận, 366 ngày.")
else:
    print("Đây không phải là năm nhuận, 365 ngày.")

# Exercise 2: Kiểm tra tháng có bao nhiêu ngày
x = int(input("Tháng mấy? "))
if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
    print("Tháng này có 31 ngày.")
elif x == 2:
    y = int(input("Năm nào? "))
    if y % 4 == 0:
        print("Tháng này có 29 ngày.")
    else:
        print("Tháng này có 28 ngày.")
else:
    print("Tháng này có 30 ngày.")

# Exercise 3: Kiểm tra tháng này là mùa gì
x = int(input("Tháng mấy? "))
if 1 <= x <= 3:
    print("Đây là mùa xuân.")
elif 4 <= x <= 6:
    print("Đây là mùa hè.")
elif 7 <= x <= 9:
    print("Đây là mùa thu.")
else:
    print("Đây là mùa đông.")  

# Excercise 4: Sắp xếp 3 số
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
if a < b < c: 
    print(a, b, c) 
elif a < c < b:
    print(a, c, b)
elif b < a < c:
    print(b, a, c)
elif b < c < a:
    print(b, c, a)
elif c < a < b:
    print(c, a, b)
else:
    print(c, b, a)

# Exercise 5: Kiểm tra 3 số có tạo thành 3 cạnh của tam giác 
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
if a < b + c and b < a + c and c < a + b:
    print("3 số này tạo thành tam giác.")
    if a == b == c:
        print("3 số này tạo thành tam giác đều.")
    elif a == b or a == c or b == c:
        print("3 số này tạo thành tam giác ")
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        print("3 số này tạo thành tam giác vuông.")
    else:
        print("3 số này tạo thành tam giác thường.")
else:
    print("3 số này không tạo thành tam giác.")

# Exercise 6: Tính tiền điện
x = float(input("Nhập số điện: "))
if 0 <= x <= 50:
    print("Số tiền điện: ", 1678 * x, "VND")
elif 51 <= x <= 100:
    print("Số tiền điện: ", 1734 * (x - 50) + 50 * 1678, "VND")
elif 101 <= x <= 200:
    print("Số tiền điện: ", 2014 * (x - 100) + 50 * (1678 + 1734), "VND")
elif 201 <= x <= 300:
    print("Số tiền điện: ", 2536 * (x - 200) + 50 * (1678 + 1734) + 100 * 2014, "VND")
elif 301 <= x <= 400:
    print("Số tiền điện: ", 2834 * (x - 300) + 50 * (1678 + 1734) + 100 * (2014 + 2536), "VND")
else:
    print("Số tiền điện: ", 2927 * (x - 400) + 50 * (1678 + 1734) + 100 * (2014 + 2536 + 2834), "VND")
