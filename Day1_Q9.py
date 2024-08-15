#To calculate compound interest
principal_amt=float(input("Enter the principal amount:"))
rate_interest=float(input("Enter the rate of interest:"))
num_yrs=float(input("Enter the number of years:"))
tot_amt=principal_amt*((1+(rate_interest/100))**num_yrs)
com_int=tot_amt-principal_amt

print("The compund interst is:",round(com_int,2))