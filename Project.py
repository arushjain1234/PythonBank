import re
import qrcode
from colorama import init, Fore

# Initialize balance in INR
balance = 10000  # Initial balance for demonstration purposes

# Initialize transaction history list
transactions = []

# Initialize colorama
init(autoreset=True)

# Function to display menu
def display_menu():
    print(Fore.CYAN + "\nPython International Bank Menu:")
    print("1. " + Fore.BLUE + "Check Balance")
    print("2. " + Fore.GREEN + "Deposit")
    print("3. " + Fore.RED + "Withdraw")
    print("4. " + Fore.YELLOW + "View Transactions")
    print("5. " + Fore.MAGENTA + "BHIM UPI Payment")
    print("6. " + Fore.BLUE + "Credit Card Payment")
    print("7. " + Fore.GREEN + "Generate QR Code for your UPI")
    print("8. " + Fore.RED + "Exit")

# Function to check balance
def check_balance():
    print(f"Current balance: ₹{balance}")

# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter deposit amount in INR: ₹"))
    balance += amount
    transactions.append(("Deposit", amount))
    print(f"Deposited ₹{amount}. Current balance: ₹{balance}")

# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount in INR: ₹"))
    if amount > balance:
        print(Fore.RED + "Insufficient funds! Withdrawal cancelled.")
    else:
        balance -= amount
        transactions.append(("Withdrawal", amount))
        print(f"Withdrew ₹{amount}. Current balance: ₹{balance}")

# Function to view transactions
def view_transactions():
    print("\n" + Fore.YELLOW + "Transaction History:")
    for index, transaction in enumerate(transactions, start=1):
        print(f"{index}. {transaction[0]}: ₹{transaction[1]}")
        if transaction[0] == 'Deposit' or transaction[0] == 'Withdrawal':
            print(f"These are your details: \nAmount: ₹{transaction[1]}\nCurrent balance: ₹{balance}")
        elif transaction[0] == 'Credit Card Payment':
            print(f"These are your details: \nAmount: ₹{transaction[1]}\nRecipient: {transaction[2]}")
        else:
            print(f"These are your details: \nAmount: ₹{transaction[1]}")

import re
from colorama import Fore

# Function to validate UPI ID format
def validate_upi_id(upi_id):
    # Regular expression pattern for UPI ID validation
    pattern = r"^[_]{10}@okpib$"
    return re.match(pattern, upi_id) is not None

import re
from colorama import Fore

# Function to validate UPI ID format
def validate_upi_id(upi_id):
    # Regular expression pattern for UPI ID validation
    pattern = r"^[a-zA-Z0-9_]{1,10}@okpib$"
    return re.match(pattern, upi_id) is not None

# Function for BHIM UPI Payment
def bhim_upi_payment():
    global balance
    amount = float(input("Enter payment amount in INR: ₹"))
    if amount > balance:
        print("Insufficient funds! Payment cancelled.")
        return
    
    upi_id = input("Enter recipient's UPI ID (__________@okpib): ")
    if not validate_upi_id(upi_id):
        print("Invalid UPI ID format! Please enter a UPI ID with up to 10 characters followed by '@okpib'.")
        return
    
    # Simulating a successful payment
    balance -= amount
    transactions.append(("BHIM UPI Payment to " + upi_id, amount))
    print(f"Payment of ₹{amount} sent to {upi_id}. Current balance: ₹{balance}")


# Function for Credit Card Payment
def credit_card_payment():
    global balance
    amount = float(input("Enter payment amount in INR: ₹"))
    if amount > balance:
        print(Fore.RED + "Insufficient funds! Payment cancelled.")
    else:
        card_number = input("Enter card number (12 digits, e.g., 1234 5678 9012): ").replace(' ', '')
        cvv = input("Enter CVV (3 digits, e.g., 123): ").replace(' ', '')
        
        # Check if card number and CVV are of correct length
        if len(card_number) != 12 or len(cvv) != 3:
            print(Fore.RED + "Invalid card number or CVV! Payment cancelled.")
        else:
            # Check if card number contains only digits and CVV contains only digits
            if not card_number.isdigit() or not cvv.isdigit():
                print(Fore.RED + "Invalid card number or CVV! Payment cancelled.")
            else:
                recipient = input("Enter the name of the recipient company: ")
                balance -= amount
                transactions.append(("Credit Card Payment", amount, recipient))
                print(f"Payment of ₹{amount} made via credit card to {recipient}. Current balance: ₹{balance}")

# Function to generate user's QR code
def generate_qr_code():
    user_name = input("Enter your name: ")
    upi_id = input("Enter your UPI ID (_________@okpib): ")
    if upi_id.endswith("@okpib") and len(upi_id) <= 10:
        # Assume bank's UPI ID is "pythonbank@okpib" for demonstration
        bank_upi_id = "pythonbank@okpib"
        user_qr_data = f"Name: {user_name}\nUPI ID: {upi_id}\nBank's UPI ID: {bank_upi_id}"
        qr_code = qrcode.make(user_qr_data)
        qr_code.show()
    else:
        print(Fore.RED + "Invalid UPI ID format! QR code generation cancelled.")


# Main function
def main():
    print(Fore.CYAN + "Welcome to Python International Bank!")
    while True:
        display_menu()
        choice = input(Fore.MAGENTA + "Enter your choice: ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            view_transactions()
        elif choice == '5':
            bhim_upi_payment()
        elif choice == '6':
            credit_card_payment()
        elif choice == '7':
            generate_qr_code()
        elif choice == '8':
            print(Fore.RED + "Thank you for using Python International Bank!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
