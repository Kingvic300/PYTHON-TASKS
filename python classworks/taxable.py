print("0-> Single filers,\n1-> married filing jointly,\n2-> married filing separately,\n3-> head of households\n") 
	
number = float(input("Enter the filing status "))
taxable = float(input("Enter taxable income  ")) 
taxs = 0
if number == 0:
	if taxable>0 and taxable < 8350 :
		taxs = taxable * 0.1
		print(taxs)
	elif taxable > 8351 and taxable < 33950:
		tax = 8350 * 0.10
		taxable -= 8350
		tab = taxable * 0.15
		table = tax + tab
		print(table)