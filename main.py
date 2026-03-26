import streamlit as st
import random

# Store data in session
if "bankData" not in st.session_state:
    st.session_state.bankData = {}

bankData = st.session_state.bankData

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Check Statement",
        "Update Details",
    ],
)

# ------------------ CREATE ACCOUNT ------------------
if menu == "Create Account":
    st.header("Create New Account")

    name = st.text_input("Enter Name")
    mobile = st.text_input("Enter Mobile Number")
    adhar = st.text_input("Enter Adhar Number")
    age = st.number_input("Enter Age", min_value=1)
    amount = st.number_input("Enter Initial Amount", min_value=0)

    if st.button("Create Account"):
        account_number = random.randint(1000, 9999)

        bankData[account_number] = {
            "Name": name,
            "Mobile_number": mobile,
            "AdharCard_number": adhar,
            "Age": age,
            "Amount": amount,
            "Account_number": account_number,
        }

        st.success("Account Created Successfully!")
        st.info(f"Your Account Number is: {account_number}")

# ------------------ DEPOSIT ------------------
elif menu == "Deposit Money":
    st.header("Deposit Money")

    acc_no = st.number_input("Enter Account Number", step=1)

    if acc_no in bankData:
        amount = st.number_input("Enter Deposit Amount", min_value=0)

        if st.button("Deposit"):
            bankData[acc_no]["Amount"] += amount
            st.success("Amount Deposited Successfully")
            st.write("Total Balance:", bankData[acc_no]["Amount"])
    else:
        st.warning("Account Not Found")

# ------------------ WITHDRAW ------------------
elif menu == "Withdraw Money":
    st.header("Withdraw Money")

    acc_no = st.number_input("Enter Account Number", step=1)

    if acc_no in bankData:
        amount = st.number_input("Enter Withdraw Amount", min_value=0)

        if st.button("Withdraw"):
            if bankData[acc_no]["Amount"] >= amount:
                bankData[acc_no]["Amount"] -= amount
                st.success("Money Withdrawn Successfully")
                st.write("Remaining Balance:", bankData[acc_no]["Amount"])
            else:
                st.error("Insufficient Balance")
    else:
        st.warning("Account Not Found")

# ------------------ STATEMENT ------------------
elif menu == "Check Statement":
    st.header("Check Bank Statement")

    acc_no = st.number_input("Enter Account Number", step=1)

    if acc_no in bankData:
        data = bankData[acc_no]

        st.subheader("Account Details")
        st.write("Name:", data["Name"])
        st.write("Mobile:", data["Mobile_number"])
        st.write("Adhar:", data["AdharCard_number"])
        st.write("Age:", data["Age"])
        st.write("Balance:", data["Amount"])
    else:
        st.warning("Account Not Found")

# ------------------ UPDATE ------------------
elif menu == "Update Details":
    st.header("Update Account Details")

    acc_no = st.number_input("Enter Account Number", step=1)

    if acc_no in bankData:
        option = st.selectbox(
            "Select Field",
            ["Name", "Mobile_number", "AdharCard_number", "Age"],
        )

        new_value = st.text_input("Enter New Value")

        if st.button("Update"):
            if option == "Age":
                new_value = int(new_value)

            bankData[acc_no][option] = new_value
            st.success(f"{option} Updated Successfully")
    else:
        st.warning("Account Not Found")