#to convert days into years,weeks and days
days=int(input("Enter the days:"))
yrs=days//365
rem_days=days%365
weeks=rem_days//7
rem_days=rem_days%7

print(f"Years:{yrs} \nWeeks:{weeks} \nDays:{rem_days}")