#to find min and max in list of numbers
list_num=input("Enter the numbers seperated by spaces:")
int_num=list(map(int,list_num.split()))

print("Maximum:",max(int_num))
print("Minimum:",min(int_num))