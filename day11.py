#Required Libraries:

import pandas as pd
df = pd.read_csv("accounts.csv")
print(df)

def compound_interest (principal,rate,time):
    ci = principal * (1+rate/10) ** time
    return ci

#From User:


# Need of the code:

for index , account in df.iterrows():
    ci = compound_interest(account["principal"],account["rate"],account["time"])
    print(f"Details of account : Holder : {account['name']} , Initial Amount : {account['principal']} , Interest_Compounded : {round(ci-account['principal'],2)} , Total Amount : {round(ci,2)}")
    df.loc[index, "balance"] = ci

print(round(df["balance"].max()),2)
print(round(df["balance"].min()),2)
print(round(df["balance"].mean()),2)
df.info()
df.describe()
print(df[["name","balance"]])
