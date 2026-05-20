#Block Part:

def simple_interest(principal, rate , time):
    si= principal * rate * time / 100
    return si

#Input Part:

time = int(input("Enter The time in years: "))

#Accounts "n" Loop Part:

acc_1 = {"Name": "Nehan" , "Account": 5000 , "Rate": 8}
acc_2 = {"Name": "Sahil" , "Account": 12000 , "Rate": 10}
acc_3 = {"Name": "Rohit" , "Account": 8500 , "Rate": 9}

accounts = [acc_1 , acc_2 , acc_3]
for account in accounts:
    rate_of_interest = round(simple_interest(account["Account"] , account["Rate"] , time),2)
    print(f" Name = {account['Name']} ,  Account ={account['Account']} , Interest = {rate_of_interest}")