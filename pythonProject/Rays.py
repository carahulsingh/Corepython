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
# def sum(a,b):
#     return a+b
# def mul(a,b):
#     return a*b
# def sub(a,b):
#     return a-b
# def dev(a,b):
#     if b==0:
#         return "error!Devision by Zero"
#     else:
#         return a/b
# def calculator():
#     print("select operation")
#     print("1. sum")
#     print("2. mul")
#     print("3. sub")
#     print("4. dev")
#
#     choice = input("enter choice (1/2/3/4):")
#     num1 = float(input("enter first number: "))
#     num2 = float(input("Enter second number: "))
#
#     if choice == '1':
#         print("result:", sum(num1, num2))
#     elif choice=='2':
#         print("result", mul(num1,num2))
#     elif choice =='3':
#         print("result",sub(num1,num2))
#     elif choice =='4':
#         print("result",dev(num1,num2))
#     else:
#         print("invalid input")
#
# calculator()
#
# def add(firstname,lastname):
#     print("adding user name")
#     print("name",firstname,lastname)
#
# def update(firstname,lastname):
#     print("update user name")
#     print("name",firstname,lastname)

# def sumNum(a,*varg):
#     t=a
#     for n in varg:
#         t+=n
#     return t
# total=sumNum(2,4,5,10,11,15)
# print(total)


### kisi function me key and value dono print krane ke liye
# def my_function(** module):
#     for key,value in module.items():
#         print(f"this is key value={key}:this is value = {value}")
#
# my_function(a=1,b=2,c=3,d="shivam",e="rahul")

####### * and ** ek sath run krne k liye
#
# def my_function(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
#
# my_function(1,2,3,4,a=4,b="mohan")

# def my_function(** module):
#     for key,value in module.items():
#         print(f"first name ={key}:last name = {value}")
#
# my_function(rahul="rajawat")

# def my_function(** module):
#     for key,value in module.items():
#         print(f"{key}:{value}")
# f = input("enter your first name :")
# l = input("enter your last name:")
#
# my_function(name=f, surname=l)
# print("welcome",f,l,"!")
#
# def my_function(** module):
#     for key,value in module.items():
#         return(f"{key}:{value}")
# f = input("enter your first name :")
# l = input("enter your last name:")
#
# my_function(name=f, surname=l)
# print("welcome",f,l,"!")

######### class ka first letter capital hi lena he (example Person ka P capital he )
# class person:
#     def set_details(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def introduce(self):
#         print(f"Hello, my name is {self.name}. i am {self.age} years old and {self.gender}.")
#
# class vehicle_details:
#     def car(self,color,company):
#         self.color = color
#         self.company = company
#
#     def showinfocar(self):
#         print(f"hello this my car color {self.color}. my car company name {self.company}.")
#
# p = person()
# p.set_details(input("name"),input("age"),input("gender"))
#
# # calling methods on the person object
# #### self = this is refrence parameter
# ### p jo he object he class person() ka
# #### object calling
# ###p= person()
# ### p.lagakar aap person class k function & methods ko call kr skte he
#
# p1 = vehicle_details()
# p1.car(input("car color"), input("company name"))
# # calling methods on the car object
# p.introduce()
# p1.showinfocar()


###### constructor
# class Account:
#     def __init__(self, account_holder, initial_balance=0):
#         self.acc_holder = account_holder
#         self.balance = initial_balance
#
# acc1 = Account("bharat",1000.99)
# print("Acoount Holder:",acc1.acc_holder)
# print("Initial Balance:", acc1.balance)


### constructor ke sath input command
# class Account:
#     def __init__(self, account_holder, initial_balance=0):
#         self.acc_holder = account_holder
#         self.balance = initial_balance
#
# acc1 = Account(input("account Name"),input("Initial Balance"))
# print("Acoount Holder:",acc1.acc_holder)
# print("Initial Balance:", acc1.balance)

##### using methods and constructor

# class Person:
#     def __init__(self,name,age,gender):
#         self.NAME = name
#         self.AGE = age
#         self.GENDER = gender
#     def greet (self):
#         return f"hello, my name is {self.NAME} and i am {self.AGE} years old."
#
#     def get_gender(self):
#         return f"i am {self.GENDER}."
#
# ### create an instance of Person
# person1 = Person(input("name:"),input("age:"),input("gender"))
#
# ### Access attributes and call methods
# print(person1.greet())
# print(person1.get_gender())


#### inheriting - 1 class ki property ko dusri class me use krna

# class A:
#     def method_A(self):
#         print("method A from class A")
#
# class B(A):
#     def method_B(self):
#         print("Method B from class B")
#
# class C(B):
#     def method_C(self):
#         print("Method C from class C")
#
# ## creating an instance of class C
# obj_c = C()
#
# ## Accessing methos of all classes
# obj_c.method_A()   # accessing method of class A
# obj_c.method_B()   # accessing method of class B
# obj_c.method_C()   # accessing method of class C

# #### agar user se 10 digit mobile no. input chahiye keval integer value hi lena ho
# def is_valid_integer(input_str):
#     #check if the input string represent an integer
#     try:
#         int(input_str)
#         return True
#     except ValueError:
#         return False
# def main():
#     user_input = input("Please enter a 10-digit number: ")
#     # check if the input is a numeric string
#     if is_valid_integer(user_input):
#         # check if the input has exactly 10 digits
#         if len(user_input) == 10:
#             print("valid input. You entered a 10-digit number:", user_input)
#         else:
#             print("Invalid input. Please enter a 10-digit number.")
#     else:
#         print("Invalid input. Please enter an integer.")
#
# if __name__ == "__main__":
#     main()

##### inheritence

# class Shape:
#     def __init__(self,color):
#         self.color = color
#     def area(self):
#         pass
#     # pass function ka use kisi bhi function ko chhod kr us class ke dusre function ko call krne ke liye krte he
#
# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.radius = radius
#         ### Super(). ka use parant class ke constructor ko call krne ke liye krte he
#     def area(self):
#         return 3.14 * self.radius ** 2
# circle = Circle("red", 5)
# print("circle color:", circle.color)
# print("circle radius:", circle.radius)
# print("circle area:", circle.area())

# class Shape:
#     def __init__(self,color):
#         self.color = color
#     def area(self):
#         pass
#     # pass function ka use kisi bhi function ko chhod kr us class ke dusre function ko call krne ke liye krte he
#
# class Rectangle(Shape):
#     def __init__(self, color, hight, width):
#         super().__init__(color)
#         self.hight = hight
#         self.width = width
#
#         ### Super(). ka use parant class ke constructor ko call krne ke liye krte he
#     def area(self):
#         return self.width * self.hight
# circle = Rectangle("red", 5, 4)
# print("circle color:", circle.color)
# print("circle hight:", circle.hight)
# print("circle width:", circle.width)
# print("circle area:", circle.area())

