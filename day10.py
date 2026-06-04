import pandas as pd 
df = pd.read_csv("accounts.csv")
print(df)

def compound_interest(principal , rate , time):
    ci = principal * (1 + rate/100) ** time
    return ci

for index , account in df.iterrows():
    ci  = compound_interest(account["principal"] , account["rate"] , account["time"])
    print(f"Details of Account Holder : {account['name']} , Initial Amount : {account['principal']} , Compound Interest : {round(ci - account['principal'],2)} , Total Amount : {round(account['principal']+ci,2)}")

Low_Value =  (df[df["principal"] < 15000])
High_Value = (df[df["principal"] > 10000])
print("High Value :")
print(High_Value)
print("Low Value :")
print(Low_Value)