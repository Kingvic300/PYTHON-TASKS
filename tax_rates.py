print("  0-> Single filers,\n  1-> married filing jointly,\n  2-> married filing separately,\n  3-> head of households\n") 
	
number = float(input("Enter the filing status "))
taxable = float(input("Enter taxable income  ")) 
tax = 0
if number == 0:
	print("You selected single filers")
	if taxable > 0 and taxable < 8350 :
		tax = (taxable * 0.10)
		print(tax)

	elif taxable > 8351 and taxable < 33950:
		tax = (8350 * 0.10) + (taxable - 8350)* 0.15
		print(tax)

	elif taxable > 33951 and taxable < 82250:
		tax = (8350 * 0.10) + ((taxable - 8350)* 0.15) + ((taxable - 33950)*0.25)
		print(tax)

	elif taxable > 82251 and taxable < 171550:
		tax = (8350 * 0.10) +(taxable - 8350)* 0.15 + (taxable - 33950)*0.25 + (taxable - 82250)*0.28
		print(tax)

	elif taxable > 171551 and taxable < 372950:
		tax = (8350 * 0.10) + (taxable - 8350)*0.15 + (taxable - 33950)*0.25 +(taxable - 82250)*0.28 + (taxable - 171550)*0.33
		print(tax)

	elif taxable > 372951:
		tax = (8350 * 0.10) + (taxable - 8350)*0.15 +(taxable - 33950)*0.25 +(taxable -82250)*0.28 + (taxable - 171550)*0.33 + (taxable - 372950)*0.35
		print(tax)
		
if number == 1:
	print("You selected married filing jointly ")
	if taxable > 0 and taxable < 16700 :
		tax = (taxable * 0.10)
		print(tax)

	elif taxable > 16701 and taxable < 67900:
		tax = (16700 * 0.10) + (taxable - 16700)* 0.15
		print(tax)

	elif taxable > 67901 and taxable < 137050:
		tax = (16700 * 0.10) + (taxable - 16700)* 0.15 + (taxable - 67900)*0.25
		print(tax)

	elif taxable > 137051 and taxable < 208850:
		tax = (16700 * 0.10) +(taxable -16700)* 0.15 + (taxable - 67900)*0.25 + (taxable - 137050)*0.28
		print(tax)

	elif taxable > 208851 and taxable < 372950:
		tax = (16700 * 0.10) + (taxable - 16700)*0.15 +(taxable - 67900)*0.25 +(taxable -137050)*0.28 + (taxable - 208850)*0.33
		print(tax)

	elif taxable > 372951:
		tax = (16700 * 0.10) + (taxable - 16700)*0.15 +(taxable - 67900)*0.25 +(taxable -137050)*0.28 + (taxable - 208850)*0.33 + (taxable - 372951)*0.35
		print(tax)
		
		
	
		