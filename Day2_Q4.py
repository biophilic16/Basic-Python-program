#To find the sum and average of a given list of numbers
nums=input("Enter numbers separated by spaces:")
numb=list(map(int,nums.split()))
total=sum(numb)
avg=total/(len(numb))
print(f"Sum:{total}\nAverage:{avg}")