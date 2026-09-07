while True:
    try:
        age=int(input("enter your age:"))
        break2
    except ValueError:
        print("Invalid input.Please enter a valid integer.")

        print("Your age is",age)



