"""
PSEUDO CODE
	ask the user the amount he wants to deposit with the amount of times he wants to deposit and store it	
	ask the user the amount he wants to withdraw with the  amount of time he wants to withdraw  and store it
	add the amount depositd with the amount withdrawn 
	and display the output
"""
deposit = int(input("enter amount to deposit: "))
while deposit>0:
	deposit = int(input("enter amount to deposit:"))  
	deposit+=deposit
	print(deposit)
withdraw = int(input("enter amount to withdraw:"))
	if deposit>withdraw:
		print(withdraw)
	else:
		print("insuffient funds :")