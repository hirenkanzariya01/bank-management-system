import random

bankData = {}


def CreateAccount():
    print("------------CREATE NEW ACCOUNT--------------")
    print("Give Me This Information")
    name = input("Enter Your Name :- ")
    mobileNo = input("Enter Your Mobile Number:- ")
    Adhar = input("Enter AdharCard Number:- ")
    age = input("Enter Your Age :- ")
    amount = input("Enter Amount :- ")
    account_number = random.randint(1000, 9999)

    bankData[account_number] = {
        "Name": name,
        "Mobile_number": mobileNo,
        "AdharCard_number": Adhar,
        "Age": age,
        "Amount": amount,
        "Account_number": account_number,
    }

    print("---------------------------------------------")
    print("-------Account Created Successfully----------")
    print("Account No:- ", bankData[account_number]["Account_number"])
    print("---------------------------------------------")


def Deposite():
    print("User Want To Deposite Money")
    acc_no = int(input("enter Your Account Number:- "))

    if acc_no not in bankData:
        print("Account Not Found")
    else:
        amount = int(input("Enter Deposite Amount:- "))
        bankData[acc_no]["Amount"] = int(bankData[acc_no]["Amount"]) + amount
        print("Amount Deposite Successfully ")
        print("Total Amount is :- ", bankData[acc_no]["Amount"])


def Widthrow():
    print("User Want To Widthrow Money")
    acc_no = int(input("Enter Account No:- "))
    if acc_no not in bankData:
        print("Account Not Found ")
    else:
        amount = int(input("Enter widthrown amount:- "))

        bankData[acc_no]["Amount"] = int(bankData[acc_no]["Amount"]) - amount
        print("Money widthrow successfully")
        print("Remaining Balence is :- ", bankData[acc_no]["Amount"])


def cheackStatement():
    print("User Want To Cheack Bank Statement")
    acc_no = int(input("Enter Your Account No :- "))
    if acc_no not in bankData:
        print("Account Not Found.")
    else:
        print("Bank Data----->>>", bankData[acc_no])
        print("----------ACCOUNT HOLDER DETAILS----------")
        print("Name:- ", bankData[acc_no]["Name"])
        print("Mobile Number:- ", bankData[acc_no]["Mobile_number"])
        print("Adhar No:- ", bankData[acc_no]["AdharCard_number"])
        print("Savings  :- ", bankData[acc_no]["Amount"])


def updateDetails():
    print("User Want To Update Details ")
    acc_no = int(input("Enter Account No :- "))
    if acc_no in bankData:
        print("============SELECT OPTIONS==========")
        print("1 for Update Name ")
        print("2. for Mobile Number ")
        print("3. for Adharcard Number ")
        print("4. for Age ")
        choice = int(input("Please Select Your Choice:- "))

        if choice == 1:
            print("user Want to update name")
            newName = input("Enter New Name :- ")
            bankData[acc_no]["Name"] = newName
            print("-----------Name Update Successfully--------------", bankData[acc_no])
            print("New Name", bankData[acc_no]["Name"])

        elif choice == 2:
            print("user Want to update mobile number")
            newMobileNo = input("Enter New Mobile Number :- ")
            bankData[acc_no]["Mobile_number"] = newMobileNo

            print("-----------Name Update Successfully--------------", bankData[acc_no])
            print("New Mobile number", bankData[acc_no]["Mobile_number"])

        elif choice == 3:
            print("user Want to update adhar number")
        elif choice == 4:
            print("user Want to update age ")
        else:
            print("Invalid Choice")

    else:
        print("Account Not Found")


def exit():
    print("Thanks For Visit ")


while True:
    print("---------------------------------------------")
    print("------------WELCOME TO THE BANK--------------")
    print("---------------------------------------------")
    print("\n")
    print("1. For Create Account:- ")
    print("2. For Deposite Money:- ")
    print("3. For Widthrow Money:- ")
    print("4. For Chack Bank Statement:- ")
    print("5. For Update Details:- ")
    print("6. For Exit")
    print("\n")

    choice = int(input("Enter Your Choice:- "))

    if choice == 1:
        CreateAccount()
    elif choice == 2:
        Deposite()
    elif choice == 3:
        Widthrow()
    elif choice == 4:
        cheackStatement()
    elif choice == 5:
        updateDetails()
    elif choice == 6:
        exit()
        break
    else:
        print("Enter Valid Choice ")
