number = int(input("Enter your unit of electricity used "))
first = number - 100
second = 100*50
if number<100:
	print("no charge")
if number > 100:
	second_units = first - 100
	price  = second_units*100
	total_price = second + price  
	print(total_price)
	
	