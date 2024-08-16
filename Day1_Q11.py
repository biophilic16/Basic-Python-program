#find sum of all positive numbers
num=input("Enter the numbers seperated by spaces:")
int_num=list(map(int,num.split()))
sum=0
for x in int_num:
    if x>=0:
        sum+=x

print("Sum:",sum)        