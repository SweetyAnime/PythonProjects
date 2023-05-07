#if user email is nk2022@gmail.com and pass is 29042003
email_address = str(input("enter email address :"))
if email_address.endswith("@gmail.com") and email_address=="nk2022@gmail.com":
    print("Okay :)")
else:
    print("@gmail.com Missing or Wrong Email Id")
password = str(input("enter password:"))
if password=="29042003":
    print(f"Welcome {email_address} :)")
else:
    print("Wrong Password")
#incomplete