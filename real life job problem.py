#real life job problem:
per_day_salary=300
day_work=int(input("enter a your work day"))
#find total salary in one month:
total_salary=per_day_salary*30
print("total_salary:",total_salary)
#your total one month salary:
your_total_salary=day_work*per_day_salary
print("your_total_salary:",your_total_salary)
#how much your salary cut:
cut_off_salary=total_salary-your_total_salary
print("cut_off_salary:",cut_off_salary)
#your days off
day_off=30-day_work
print("day_off:",day_off)
#minimum day work
min_day=15
if day_work>min_day:
    print("good worker!")
elif day_work==min_day:
    print("need more day work")
else:
    print("your are fire in this job") 


