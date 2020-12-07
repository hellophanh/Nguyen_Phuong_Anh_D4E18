store = ["","Hoodie", "T-shirt"]
welcome = str(input("Welcome to our shop, what do you want? (C R U D): "))

while welcome == "C" or welcome == "c" or welcome == "D" or welcome == "d" or welcome == "U" or welcome == "u" or welcome == "r" or welcome == "R":
    if welcome == "C" or welcome == "c":
        new_stuff = str(input("Enter new stuff: "))
        store.append(new_stuff)
        
        for i in range(1, len(store)):
            print(f'{i}.{store[i]}')
        welcome = str(input("To exit our store, type 'EXIT', else press (C, R, U, D): ")) 

    elif welcome == "R" or welcome == "r":
        for i in range(1, len(store)):
            print(f'{i}.{store[i]}')
        welcome = str(input("To exit our store, type 'EXIT', else press (C, R, U, D): ")) 

    elif welcome == "U" or welcome == "u":
        a = int(input("Enter the position you want to update: "))
        store[a] = str(input("Enter new stuff: "))
        for i in range(1, len(store)):
            print(f'{i}.{store[i]}')
        welcome = str(input("To exit our store, type 'EXIT', else press (C, R, U, D): ")) 

    elif welcome == "D" or welcome == "d": 
        b = int(input("Position you want to delete: "))
        store.pop(b)
        for i in range(1, len(store)):
            print(f'{i}.{store[i]}')
        welcome = str(input("To exit our store, type 'EXIT', else press (C, R, U, D): ")) 
    
    else:
        print("Thank you for shopping with us!")
    
    if welcome == "EXIT":
        print("Thank you for shopping with us!")