# list=("rahul",1,2,3)
# print(list)
# list1=('a', "raj",9,8,7)
# print(list1)
# list2=list+list1
# print(list2)
# D = 1200
# D1 = 1000
# D3 = D*D1
# print("multification of D and D1 =", D3)
# price = 110
# money = 99
# if(money>price):
#     print("i can buy pizza")
#     print("enjoy my pizza")
# else:
#     print("i can't buy pizza")
#     print("filling very bad")
#
# tea=20
# coffe=50
# money=100
# a=money / tea
# b=money / coffe
# if(money>tea):
#     print("i can buy",a,"no. of Tea")
# elif(money)
# else:
# #     print("i can't buy")
# #### while
# num=1
# num += 1
# while (num < 10):
# #     print(num)
#
# num = 1
#
# while (num<101):
#     print(num)
# #     num+=1
#
# num=1
# while (num <101):
#     print(num)
#     num+=2

# num=100
# while  (num>0):
#     print(num)
#     num-=1

# num=100
# while(num>0):
#     print(num)
#     num-=2

#reverse
# num=100
# while  (num>=0):
#     if(num% 2 ==0):
#         print(num)
#     num -=1
# num=0
# sum=0
# while(num<=10):
#     num=num+1
#     sum=sum+num
#     print(num)
# print("sum of first 10 numbers",sum)
# num=5
# print(num --10)
# # for loop
# for i in range(1,101):
#     print(i)


# odd value print krwane ke liye
# for i in range(1,100):
#     if(i % 2 == 0):
#         print(i)

# reverse counting
# for i in range (100,0,-1):
#     print(i)

# odd value print krwane ke liye 2 method
# for i in range (0,100,+2):
#     print(i)

#rays indore ke sare word ko ek k niche ek print krwane ke liye
# world = "rays indore"
# for letters in world:
#     print(letters)

# list ke letters ko print krwane ke liye
# l=(1,2,3,"Ram","Shyam","Rays")
# for letters in l:
#     print(letters)

# list ke andr ki list k sare leters print krne ke liye
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for letters in matrix:
#     for rahul in letters:
#         print(rahul)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for letters in matrix:
#     for num in letters:
#         if (num%2==0):
#             print(num)

# kisi user k input number k aage msg print krwane k liye
# num = int(input("enter a number"))
# if num >=0:
#     print(num,"is a positive number")
# else:print(num,"is a nagetive number")

# interger ko float me convert krne ke liye
# x=5
# y=float(x)
# print("value of y",y)

# float ko integer me convert krne ke liye
# x='5'
# y=int(x)
# print("value of y",y)

# float ko integer me convert krne ke liye
# x= 7.50
# y=int(x)
# print("value of y",y)

# integer ko string me convert krne ke liye
# x= 123
# y=str(x)
# print("value of y",y)

# string ko integer me convert krne ke liye
# x= "123"
# y=int(x)
# print("value of y",y)

# palindrome
# 787
# jahaj
# ese word jise aage se pade ya piche se wo hamesha same rahta he
# num=(input("enter a number"))
# if num[::-1] == num:
#     print("this is a palindrome")
# else:
#     print("this is not palindrome")

### BRAKE & CONTINUE
# str="python"
# for i in str:
#     if i =='o':
#         break
#     print(i)

# str="python"
# for i in str:
#     if i =='o':
#         continue
#     print(i)


# l = ["ram","shyam","mohan",1,2,3,4,5]
# for i in l:
#     if i ==3:
#         break
#     print(i)

# l = ["ram","shyam","mohan",1,2,3,4,5]
# for i in l:
#     if i ==3:
#         continue
#     print(i)

###DATE & TIME
# import datetime
# x = datetime.datetime.now()
# print(x)

# import datetime
# x = datetime.datetime(2018,6,1)
# print(x)

# import datetime
# x = datetime.date(2018,6,1)
# print(x)

### search
# numbers= [1,2,3,4,5,6,7,8,9,10]
# search_for = 9
# for num in numbers:
#     if num == search_for:
#         print("element found")
#         break
# else:
#     print("element not found")

# num = int(input("input a numbers"))
# if num % 7==0 and num % 5 ==0:
#   print("this number devided by both")
# else:print("this number is not devided by both")

# num = int(input("input a numbers"))
# if num % 7==0 and num % 5 ==0 and num % 35 ==0:
#   print("this number devided by both")
# else:print("this number is not devided by both")

# import datetime
# x= datetime.datetime.now()
# print(x.strftime("%A"))
# print(x.strftime("%B"))

###### functions
# def sum(a,b,c):
#     d=a+b+c
#     print("sum of a,b,c =",d)
#
# sum(10,15,20)

# def sum(a,b,c):
#     d=a*b*c
#     print("sum of a,b,c =",d)
#
# sum(10,15,20)

# def sum(a,b,c):
#     d=a/b/c
#     print("sum of a,b,c =",d)
#
# sum(10,15,20)

### define a function "greet", "add", "multiply"
# def greet(a):
#     d=a
#     print("hello every one my name is",d)
# greet("rahul")
#
# def add(a,b,c):
#     d=a+b+c
#     print("sum of a,b,b =",d)
# add(10,15,50)
#
# def add(a,b,c):
#     d=a*b*c
#     print("sum of a,b,b =",d)
# add(10,15,50)


### calculator
def sum(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
def dev(a,b):
    if b==0
        return "error!Devision by Zero"
    else:
        return a/b
def calculator():
    print("select operation")
    print("1. sum")
    print("2. mul")
    print("3. sub")
    print("4. dev")

    choice = input("enter choice (1/2/3/4")
    num1 = float(input("enter first number"))
    num2 = float(input("Enter second number"))

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
