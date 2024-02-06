#britday celebration:
budget= 38000
place_price=int(input("enter a place price:"))
dinner=int(input("enter a brithday dinner price"))
decoration=int(input("enter a decoration price:"))
catering=int(input("enter a catering price:"))
total_price=place_price+dinner+decoration+catering
print("total_price:",total_price)
need_price=total_price-budget
if budget<total_price:
    print("need_Price:",need_price)
if budget>total_price:
    discount=total_price*0.5
    print("discount price:",discount)
    print("buy gift for your friend")
elif budget==total_price:
    discount=total_price*0.2
    print("discount price:",discount)
    print("celebrate a party")
else:
    print("party cancel")
    
