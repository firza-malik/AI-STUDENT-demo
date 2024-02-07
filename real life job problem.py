#logical problems:
#QUESTION NO 1:

num=int(input("enter a num:"))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print(" number is zero")


#question no 2:
age=int(input("enter your age:"))
if age<18:
    print("they are child")
elif age==18:
    print("they are teenager")
else:
    print("you are  senior citizen")


#question no 3:
num1=int(input("enter a number1;"))
num2= int(input("enter a numer2:"))
if num1>num2:
    print("num1 is largr number")
elif num2>num1:
    print("num2 is larger number")
else:
    print("both num1 and num2 are equal")

#question no 4:
year=int(input("enter a year:"))
if year%400==0:
    print("its a leap year")
elif year%4==0 and year%100!=0:
    print("its a leap year")
else:
    print("its not a leap year")

#question no 5:
num3=int(input("enter a number3;"))
num4= int(input("enter a numer4:"))
num5=int(input("enter a number5;"))
max_num=max(num3,num4,num5)
min_num=min(num3,num4,num5)
print("maximum number:",max_num)
print("minimum number:",min_num)

#question no 6:
n=int(input("enter a exam marks:"))
if n>=90:
    print("A garde")
elif n<=89 and n>=80:
    print("B garde")
elif n<=79 and n>=70:
    print("C garde")
elif n<=69 and n>=60:
    print("D garde")
else:
    print("F garde")




    


    

    
    


    
