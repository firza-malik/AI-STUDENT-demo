#simple practical problem:
#question no 1:
price1=int(input("enter a price1:"))
price2=int(input("enter a price2:"))
quantity1=int(input("enter a quantity1:"))
quantity2=int(input("enter a quantity2:"))
apple=price1*quantity1
orange=price2*quantity2
total_cost=apple+orange
print("total_cost:",total_cost)
discount=total_cost*0.1
if total_cost==1000:
    total_price=total_cost-discount
    print("total_price:",total_price)
else:
    print("total_price:",total_cost)

#question no 2:
tempurature=float(input("enter a temp:"))
if tempurature<20:
    print("they should wear a jacket!")
else:
    print("no need for a wear jacket!")    

#question no 3:
side1=float(input("enter a side1:"))
side2=float(input("enter a side2:"))
side3=float(input("enter a side3:"))
if side1==side2==side3:
    print("its equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("its a isosceles triangle")
else:
    print("its scalene triangle") 

#question no 4; 
pin_code=12345
balance=80000

user_pin_code=int(input("enter your pin code:"))
if pin_code==user_pin_code:
    withdraw_amount=int(input("enter a withdraw amount:"))
    if withdraw_amount<=balance:
        new_balance=balance-withdraw_amount
        print("withdraw successfully")
        print("your new bank balance",new_balance)
    else:
        print("insufficient balance ")
else:
    print("invalid user_pin_code")            

#question no 5:
month=int(input("enter a month:"))
if month==1:
    print("31 days")
elif month==2:
    print("29 days")
elif month==3: 
    print("31 days")
elif month==4:  
    print("30 days")
elif month==5: 
    print("31 days")
elif month==6: 
    print("30 days")
elif month==7: 
    print("31 days")
elif month==8: 
    print("31 days")    
elif month==9: 
    print("30 days")
elif month==10: 
    print("31 days")
elif month==11: 
    print("30 days")
elif month==12:
    print("31 days")   
else:
   print("invalid month") 
   
#question no 6:
year=int(input("enter a year:"))
month=int(input("enter a month:"))
if month==2:
    if year%400==0 or year%4==0 and year%100!=0:
        print("29 day")
    else:
        print("28 days")
elif month==1:
    print("31 days")
elif month==3: 
    print("31 days")
elif month==4:  
    print("30 days")
elif month==5: 
    print("31 days")
elif month==6: 
    print("30 days")
elif month==7: 
    print("31 days")
elif month==8: 
    print("31 days")    
elif month==9: 
    print("30 days")
elif month==10: 
    print("31 days")
elif month==11: 
    print("30 days")
elif month==12:
    print("31 days")   
else:
   print("invalid month")
