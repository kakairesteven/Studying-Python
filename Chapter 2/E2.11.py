import math
# final account value
final_value = eval(input("Enter final account value: "))

# Annual interest
annual_interest = eval(input("Enter annual interest rate in percent: "))

# duration in years
duration = eval(input("Enter the duration in years: "))

initialDepositAmount = final_value / math.pow(1 + (annual_interest/12/100), duration*12)

print("Initial deposit value is %.10f"%(initialDepositAmount))
