def main():
	number = int(input("enter a number:"))
	print(rider_deliveries)(number)

def rider_deliveries(number): 
        if number < 50:
            return number * 160 + 5000
        elif 50 >= number < 60:
            return number * 200 + 5000
        elif 60 >= number < 70:
            return number * 250 + 5000
        else:
            return number * 500 + 5000
