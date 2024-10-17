import time

total_Seconds = time.time()
current_Seconds = int(total_Seconds % 60)
total_Minutes  = total_Seconds/60
current_Minutes = int(total_Minutes % 60)
total_Hours = total_Minutes / 60
current_Hours = int((total_Hours % 24)+1)
print(current_Hours ,":", current_Minu.klotes ,":", current_Seconds)