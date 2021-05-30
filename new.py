import random
import emoji
"""
This programme helps the user to generate random pins and passwords for day to day use and keeps 
a record of those.
"""
def pin():
    pinsample = "123456789"
    Used = str(input("What do you intend the PIN for :"))
    passlen = int(input("Enter the length of PIN :"))
    p = "".join(random.sample(pinsample,passlen ))
    print("Your PIN for " + Used + " : " + p)
    print(Used + ":" + p, file=open('pin_output.txt','a'))
    #print(Used + ":" + p, file=open('output.XLSX','a'))
"""
The pin function executes the code to give the user a pin(numbers) of his desired length ;
while the PASSWORD function looks for the length of the password and gives the user a combination 
of upper case,lowercase ,numeric & special characters for a strong passowrd.
"""

def PASSWORD():
    Used = str(input("What do you intend the password for :"))
    passlen = int(input("Enter the length of password :"))

    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?/+-~{}][/"
    p = "".join(random.sample(s,passlen ))
    print("Your passowrd for " + Used + " : " + p)
    print(Used + ":" + p, file=open('pass_output.txt','a'))


    

def main():
    while True:
    
        utility = str(input("::Type 'PIN' for pin or 'PASSWORD' for password & 'STOP' if you want to close::"))
        utility = utility.upper()
        if utility == "PASSWORD" :
            PASSWORD()
        
        if utility == "PIN" :
            pin()
        if utility == "STOP":
            break
        else:
            print("\N{grinning face}")


     
if __name__ == '__main__':
    main()







