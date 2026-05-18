#A Block
def simple_interest(principal,rate,time):
    si = (principal * rate * time) / 100
    return si
#Working Part
time = int(input("Entter the time in years: "))
rate = float(input("Enter the rate of interest: "))
#User inputs
accounts = [5000 , 12000 , 8500] 
#The loop Part
for account in accounts:
    rate_of_interest =round(simple_interest(account , time , rate),2)
    print(f" Account = {account} , Interest = {rate_of_interest}")