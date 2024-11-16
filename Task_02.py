def calculator():
    n1 = float(input("Enter the first number : "))
    n2 = float(input("Enter the second number : "))
    op = input("Operation( + , - , * , /) : ")

    if op == '+':
        print(f"Result : {n1+n2}")
    elif op == '-':
        print(f"Result : {n1-n2}")
    elif op == '*':
        print(f"Result : {n1*n2}")
    elif op == '/':
        if n2!=0:
            print(f"Result : {n1/n2}")
        else :
            print("Error : Division by zero ")
    else :
        print("Error : Invalid Operation ")
calculator()
