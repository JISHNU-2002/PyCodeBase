amount = 24.326
print("Salary = %0.2f" %amount)
print("Salary = %0.1f" %amount)
print("Salary = %-7.1f" %amount)
print()

print("%4s%18s%10s%16s" % ("Year","Starting balance",\
"Interest","Ending balance"),"\n")

year = 2022
startBalance = 10000.259
interest = 7.565
endBalance = 17000.7896
print("%-6d%-18.2f%10.2f%16.2f" % \
(year,startBalance,interest,endBalance))
#extra number after %- is for spacing from next output