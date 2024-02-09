#question no1:
age=int(input("enter a age:"))
weight=float(input("enter a weight:"))
activity=input("enter a activity level:")
pre_KG_calories=12
activity_high=1.80
activity_low=0.55
activity_moderate=1.65
calories=weight * pre_KG_calories
if activity=="high":
     calories_goal=calories * activity_high
     print("calories goal;",calories_goal)    
elif activity=="low":
     calories_goal=calories * activity_low
     print("calories goal;",calories_goal)
elif activity =="moderate":
     calories_goal=calories * activity_moderate
     print("calories goal;",calories_goal)
else:
     print("activity level is incorrect")
#question no 2:
user_badtime=int(input("enter a badtime :(under a 24 hours)"))
user_wakeuptime=int(input("enter a wakeup time:(under a 24 hours )"))
total_sleep=user_badtime-user_wakeuptime
print("total sleep time:",total_sleep)
if total_sleep>=7:
    print("good sleep!")
else:
    print("need more sleep!")
#question no 3:
weight=float(input("enter a weight:"))
desired_level=input("enter a hydration level:")
if desired_level=="light":
     daily_hyderation=weight*0.04
     print("daily water need:",daily_hyderation)
elif desired_level=="moderate":
     daily_hyderation=weight*0.12
     print("daily water need:",daily_hyderation)
elif desired_level=="intense exercise":
     daily_hyderation=weight*0.06
     print("daily water need:",daily_hyderation)
else:
     print("desired level is invalid")

    
    

