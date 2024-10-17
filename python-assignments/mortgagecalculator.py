
MONTHLY_IN_YEARS = 12
PERCENTAGE_RATE = 100
principal = float(input("enter principal amount:"))

annual_interest_rate = float(input("enter the annual interest rate:"))

duration = int(input("enter the duration in years:"))

monthly_rate = annual_interest_rate/100/12;

number_of_months = duration*12;

numerator = monthly_rate*(1+monthly_rate)**number_of_months
	
denominator = (1+monthly_rate)**number_of_months-1

monthly_payment = principal *(numerator/denominator) 

print("your monthly payment is $", (round(monthly_payment,2)))
	
