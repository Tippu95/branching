user_input = input("Provide a number")
user_input = int(user_input)
if user_input > 1:
    for x in range(2, int(user_input/2)+1):
        if user_input % x == 0:
            print("not a prime number")
            break
    else:
        print("a prime number")
else:
    print("a prime number")