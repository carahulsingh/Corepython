# print("Hello")
# num = int(input("enter a number"))
# if num >=0:
#     print(num,"is a positive number")
# else:print(num,"is a nagetive number")

# list=["rahul","indore",1,2,3]
# print(list)
# list1=["raj",4,5,6]
# list2=list+list1
# print(list2)


# d1=100
# d2=5
# d3=d1*d2
# print("multification of d1 and d2 is", d3)


# price=100
# amount=2000
# if(amount>price):
#     print("i can buy",amount/price,"quantity")
# else:
#     print("i can not buy")


"""tea=10
coffee=20
amount=100
if (amount>=tea and amount>=coffee):
    print("i can buy either",amount/tea,"cup of tea or",amount/coffee,"cup of coffee")
if (amount>=tea and amount<coffee):
    print("i can only buy",amount/tea,"cup of tea")
if (amount<tea and amount>=coffee):
    print("i can only buy", amount/coffee,"cup of coffee")
else:
    print("i can't buy")"""

# tea=10
# coffee=20
# amount=100
# if (amount>=tea and amount>=coffee):
#     print("i can buy either",amount/tea,"cup of tea or",amount/coffee,"cup of coffee")
# if (amount>=tea and amount<coffee):
#     print("i can only buy",amount/tea,"cup of tea")
# if (amount<tea and amount>=coffee):
#     print("i can only buy", amount/coffee,"cup of coffee")
# if (amount<tea and amount<coffee):
#     print("i can't buy neither tea nor coffee")


# num = 1
# while  (num<10):
#     print(num)
#     num+= 1

# for even no.
# num=0
# while  (num<101):
#     print(num)
#     num+=2


# for odd no.
# num=1
# while  (num<100):
#     print(num)
#     num+=2


# # reverse
# num=100
# while(num>0):
#     print(num)
#     num-=1


# reverse even
# num=100
# while(num>0):
#     print(num)
#     num-=2

# reverse odd
# num=101
# while(num>0):
#     print(num)
#     num-=2

# num=0
# sum=0
# while(num<=10):
#     num=num+1
#     sum=sum+num
#     print(num)
# print("sum of first 10 num is",sum)

# # for loop
# for rahul in range (1,100):
#     print(rahul)

# odd value print krwane ke liye
# for rahul in range(1,100,+2):
#             print(rahul)


# rays indore ke sare word ko ek k niche ek print krwane ke liye
# world = "rays indore"
# for letters in world:
#     print(letters)

# # list ke andr ki list k sare leters print krne ke liye
# matrix=[["rahul",1,2,3],["indore",4,5,6],["rays",7,8,9]]
# for letters in matrix:
#     for i in letters:
#         print(i)

# kisi user k input number k aage msg print krwane k liye
# num = int(input("enter a number"))
# if num >=0:
#     print(num,"is a positive number")
# else:print(num,"is a nagetive number")

# num = int(input("money in the pocket"))
# iphone = 100000
# if num >=100000:
#            print("you can buy", num/iphone," nos. of i-phone")
# else:print("you doesn't have sufficient money to buy an i-phone, please sold 1 kidney")
#

# interger ko float me convert krne ke liye
# x=5
# y=float(x)
# print("value of y",y)


#from Rays import *
# add(rahul,rajawat)


# class Person:
#     def __init__(self,name,age, gender, profession):
#         self.NAME = name
#         self.AGE = age
#         self.GENDER = gender
#         self.PROFESSION = profession
#
#     def greets(self):
#         return f"hello everyone, my name is{self.NAME}.i am {self.AGE}.i am {self.GENDER} i am {self.PROFESSION}"
#
# p=Person("shivam",23,"mLE","ENN")
# print(p.greets())

user =int(input("mobile no"))
if user > 9999999999 or user < 1000000000:
    print("invalid no.")
else:
    print("valid no.")