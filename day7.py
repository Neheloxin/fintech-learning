#Mini Banking System :

def simple_interest(principal , rate , time):
    si = principal * rate * time /100
    return si


Num_acc = int(input("How many accounts do you want to create? : "))

accounts = []
for i in range(Num_acc):
    account = {"Name" :  str(input("Account Holder Name: ")) , "Principal" :  float(input("Enter The Principal : "))}
    Rate = float(input("The Rate of interest : "))
    Time = float(input("The Time in years : "))
    accounts.append(account)

for account in accounts:
     si = simple_interest(round(account["Principal"], 2), round(account["Rate"], 2), round(account["Time"], 2))
     print(f"Details Of Account Holder : {account['Name']} , Initial Amount : {account['Principal']} , Simple Interest : {si} , Total Amount : {account['Principal'] + si}")   



