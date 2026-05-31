import pandas as pd
df = pd.read_csv("accounts.csv")
print (df)

def compound_interest(principal , rate , time):
    ci = principal * (1 + rate/100) ** time
    return ci

for index, account in df.iterrows():
    ci = compound_interest(account["principal"] , account["rate"] , account["time"])
    print(f"Details Of Account Holder : {account['name']} , Initial Amount : {account['principal']} , Compound Interest : {round(ci - account['principal'],2)} , Total Amount : {round(ci,2)}")
    