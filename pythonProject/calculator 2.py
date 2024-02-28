### calculator
def sum(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
def dev(a,b):
    if b==0:
        return "error!Devision by Zero"
    else:
        return a/b
def calculator():
    print("select operation")
    print("1. sum")
    print("2. mul")
    print("3. sub")
    print("4. dev")

    choice = input("enter choice (1/2/3/4):")

    num1 = float(input("enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("result:", sum(num1, num2))
    elif choice=='2':
        print("result", mul(num1,num2))
    elif choice =='3':
        print("result",sub(num1,num2))
    elif choice =='4':
        print("result",dev(num1,num2))
    else:
        print("invalid input")

calculator()