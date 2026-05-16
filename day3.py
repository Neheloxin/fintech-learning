# From User
principal = float(input("Enter The Principal amount: "))
rate = float(input("Enter The Rate of the Principal: "))
time = int(input("Enter the Time in years: "))

#The Calculation Part
def compound_interest(principal,rate,time):
    ci = principal * (1 + rate/100) ** time - principal
    return ci

#The Output Part
print("The Compound_Interest is:  ", round(compound_interest(principal,rate,time)),2)