def simple_interest(principal,rate,time):
    si = (principal * rate * time) / 100
    return si
principal = float(input("Enter The Principal amount: "))
rate = float(input("Enter The Rate of Principal:  "))
time = int(input("Enter The Time given in years: "))
print("Interest earned is:" , simple_interest(principal,rate,time))