principal = float(input("enter principal amount:"))

annual = float(input("enter the annual interest rate:"))

duration = float(input("enter the duration in years:"))

monthly_rate = annual/100/12;

number_of_months = duration*12;

numerate = monthly_rate*(1+monthly_rate)**number_of_months
	
denomin = (1+monthly_rate)**number_of_months-1

payment = numerate/denomin

monthly_payment = principal * payment

print("your monthly payment is $", monthly_payment) 
	
