for x in range(1,21):
    print(x)

for y in range(21):
    if y % 2 == 0:
        print(y)

for z in range(100,0,-1):
    print(z)

for i in range(1,10):
    print()
    for j in range(1,10):
        if i * j < 10:
            print(i * j, end = "  ")
        else:
            print(i * j, end = " ")