import string
import random

allList=[string.digits,string.ascii_lowercase, string.ascii_uppercase, string.punctuation]


def generate(length):
    X=[]

    for i in range(length):
        if(i>3):
            i=random.randint(0,3)
        X.append(allList[i][random.randint(0,len(allList[i])-1)])
    random.shuffle(X)
    return "".join(X)


while True:
    try:
        length=int(input("\nEnter length of Password to generate : "))
    except:
        print("Please enter a valid input ")
        continue

    if(length < 6 ):
        print("length of 6 is suggested for strong password generation ")
        continue
    else:
        print("Here's your password : \" ", generate(length)," \"")
        ans=input("Do you want to generate another password (Y/N) : ")
        if(ans in ["Y","y","1"]):
            continue
        else:
            break

    



