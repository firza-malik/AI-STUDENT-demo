print("question no 1:")
step=1320
distance=20
calories=150
avrage_steps=step+step+step+step+step+step+step%7
total_distance=30*distance
print("avrage_steps per week",avrage_steps )
print("total_distance in one month",total_distance)

print("question no 2:")

name="cherry"
name2="orange"
price=500
price2=300
quantity=12
quantity2=6
budget=1000
total_cost=(price+price2)
if budget>=total_cost:
    print("you have enough budget")
else:
    print("you don't have enough budget")
print("question 3:")
print("cakerecipe:")
num_serving=5
ingredient="flour"
quantity=2.5
ingredient2="sugar"
quantity2=1.5
ingredient3="egg"
quantity3=2
ingredient4="chocolates"
quantity4=3
ingredient5="bakingpower"
quantity5=0.5
adjust_amount1=(quantity*num_serving)
adjust_amount2=(quantity2*num_serving)
adjust_amount3=(quantity3*num_serving)
adjust_amount4=(quantity4*num_serving)
adjust_amount5=(quantity5*num_serving)
print(f"{ingredient}:{adjust_amount1}cups")
print(f"{ingredient2}:{adjust_amount2}cups")
print(f"{ingredient3}:{adjust_amount3}eggs")
print(f"{ingredient4}:{adjust_amount4}cubes")
print(f"{ingredient5}:{adjust_amount5}teaspoon")
print("question no 4:")
genre1="comdy"
rating1=5.6
release1=2020
genre2="action"
rating2=1.8
release2=2019
genre3="horror"
rating3=3.5
release3=2018

user_genre=input("enter a movie;")
user_rating=float(input("enter a  movie rating(out of 5);"))
user_release=int(input("enter a release year:"))

if user_genre==genre1 and (user_rating-rating1)<=0.5 and user_release>=release1:
    print("you like genre1!")
elif user_genre==genre2 and (user_rating-rating2)<=0.5 and user_release>=release2:
    print("you like genre2!")
elif user_genre==genre3 and (user_rating-rating3)<=0.5 and user_release>=release3:
    print("you like genre3!")
else:
  print("you like matches")
print("question no 5:")
task1="study"
duration1=4
task2="gym"
duration2=2
task3="work"
duration3=6
each_task_time1=duration1%24
each_task_time2=duration2%24
each_task_time3=duration3%24
if each_task_time1<each_task_time2<each_task_time3:
        print("you want more time for your task1")
elif each_task_time2<each_task_time1<each_task_time3:
        print("you want more time for your task2")
elif each_task_time3<each_task_time1<each_task_time2:
        print("you want more time for your task3")
else:
    print("great job your each time task is perfect!")
        

          
