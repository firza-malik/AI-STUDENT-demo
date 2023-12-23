
#QUESTION NO 1:
i=1
number=[1,2,2,3,3,4,4,5,5,6,7,7]
last_num=[]
for i in number:
    if i not in last_num:
      last_num.append(i)
print(number)
print(last_num)        

#QUESTION NO 2:
a=[[1,3],[4,5]]
b=[[5,4],[3,2]]
for i in a:
    print(i)
for i in b:
    print(i)
    
for i in range(1):
    for j in range(1):
        c=a[i][j]+b[i][j]
        print("the sum of martix=",c)
print()        