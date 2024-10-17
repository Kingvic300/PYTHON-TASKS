

def get_investment(investment_amount, interest_rate, years):
	if investment_amount < 0 or interest_rate < 0 or years < 0:
		raise ValueError("Invalid number")
	else:
		number_of_months = years * 12
	
		monthly_interest = interest_rate / 100
	
		investment = investment_amount * (1 + monthly_interest) **number_of_months

		return investment