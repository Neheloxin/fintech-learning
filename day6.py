#Mini Banking System (Prototype):

def simple_interest(principal, rate, time):
    si =  principal * rate *  time / 100
    return si

time = int(input("Enter the time in years: "))

acc_1 = {"Name": "Nehan" , "Principal": 10000 , "Rate": 8}
acc_2 = {"Name": "Sahil" , "Principal": 15000 , "Rate": 10}
acc_3 = {"Name": "Rohit" , "Principal": 8000 , "Rate": 9}

accounts = [acc_1 , acc_2 , acc_3]

for account in accounts:
    si = simple_interest(account["Principal"] , account["Rate"] , time)
    print(f" Name : {account["Name"]} ,Initial Amount:{account["Principal"]} , Simple interest : {si} , Total Amount : {account["Principal"] + si}")