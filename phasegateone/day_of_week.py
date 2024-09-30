day = input("Enter today's day ")
days = input("Enter number of days after today for a future day ")
if day == "0":
	print("Today is Sunday")
elif day == "1":
	print("Today is Monday")
elif day == "2":
	print("Today is Tuesday")
elif day == "3":
	print("Today is Wednesday")
elif day == "4":
	print("Today is Thursday")
elif day == "5":
	print("Today is Friday")
elif day == "6":
	print("Today is Saturday")

if days== "0" or days== "7" or days== "14" or days== "21" or days== "28":
	print("The Future day is Monday")

elif days== "1" or days== "8" or days== "15" or days== "22" or days== "29":
	print("The Future day is Tuesday")

elif days== "2" or days== "9" or days== "16" or days== "23" or days== "30":
	print("The Future day is Wednesday")

elif days== "3" or days== "10" or days== "17" or days== "24" or days== "31":
	print("The Future day is Thursday")

elif days== "4" or days== "11" or days== "18" or days== "25":
	print("The Future day is Friday")

elif days== "5" or days== "12" or days== "19" or days== "26":
	print("The Future day is Saturday")

elif days== "6" or days== "13" or days== "20" or days== "27":
	print("The Future day is Sunday")
else:
	print("It must not exceed the days of the months ")