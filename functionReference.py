'''def say_hi(): #function definition
    print("Hi, how r u?")
say_hi()       #function calling


#2
def say_hi(): #function definition
    return("Hi, how r u?")
y=say_hi()       #function calling
print(y)

#3
def say_hi():        #function definition
    return("Hi, how r u?")
print(say_hi())       #function calling


#4
def showNumber(number):  #argument
    return "1" +number #return the value
evenNo=input("type number: ")
print(showNumber(evenNo))

#5 append to list
number=[]
def appendtoList(n):
    n.append(10)
    return n
print(appendtoList(number))

#6 square function
x = int(input("Give a input;"))
def sqr(b):
    return b**2
print(sqr(x))
'''
#map is a built-in function used for iterative arguments

x1 = int(input("Give a input;"))
x2 = int(input("Give a input;"))
x3 = int(input("Give a input;"))
list1 =[x1, x2, x3]
def sqr(n):
    return n**2
print(list(map(sqr,list1)))
