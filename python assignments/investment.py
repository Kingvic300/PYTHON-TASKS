

def get_investment(investment_amount, yearly_interest_rate, years):
	
	if yearly_interest_rate < 0 or years < 0 or investment_amount < 0:
		raise ValueError("ERRROR")

	else:

		monthly_interest_rate = float((yearly_interest_rate/100)/12)

		return round((investment_amount * (1 + monthly_interest_rate) ** (years*12)),3)

	
	