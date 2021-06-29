
def validateEmail(email):
    if (email.count("@") != 1):
        return False
    a=email.find("@")
    b=email.rfind(".")
    return True if (a!=-1 and b!=-1 and a<b and b+1<len(email)) else False


while(True):
    email=input("Enter email to slice : ")

    if(not validateEmail(email)):
        print("Provided email is not valid email..\nPlease provide an valid email.")
        continue

    else:
        print("Your entered email is",email)
        break

print("username is : ", email[:email.find("@")])
print("domain is   : ", email[email.find("@"):])

