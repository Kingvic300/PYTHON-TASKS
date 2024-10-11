initial_amount = float(input("Enter amount  "))
percentage = int(input("Enter your interest rate  "))
years = int(input("Enter years  "))
amount = 0

initial_interest = initial_amount/percentage
print("interets",initial_interest,"\n")

initial_amount = initial_amount+initial_interest
print("amount",initial_amount,"\n")


for count in range(years):
	print("Year",count+1)
	second_interest = initial_amount/percentage
	initial_interest+=second_interest
	print("interest","{:,}".format(initial_interest))

	amount+=second_interest
	initial_amount+=amount
	print("amount","{:,}".format(initial_amount),"\n")
	
#    print("Interest for year", count + 1, ": ", "{:,}".format(second_interest))
