print("Welcome to your Bank\n")

# Initialization
running = 1
balance = 500
print("Please Select from the Following Options\n\n" \
    "\t1. Make a Deposit\n" \
    "\t2. Make a Withdrawl\n" \
    "\t3. Obtain a Balance\n" \
    "\t4. Quit\n")
userName = input("Enter Name: ")

# Transaction loop
while running:
    processRun = 1
    menuSelect = input("\nMake a selection from the options menu: ")
    # Option 1
    if menuSelect == '1':
        while processRun:
            deposit = input("\nEnter amount of deposit $ ")
            if deposit.isdigit():
                balance += int(deposit)
                print("\nDeposit Processed")
                processRun = 0
            else:
                print("\nPlease enter a valid number")
    # Option 2
    elif menuSelect == '2':
        while processRun:
            withdrawal = input("\nEnter amount of withdrawal $ ")
            if withdrawal.isdigit() and int(withdrawal) < balance:
                balance -= int(withdrawal)
                print("\nWithdrawl Processed.")
                processRun = 0
            elif withdrawal.isdigit() and int(withdrawal) > balance:
                print("\nDenied. Maximum withdrawal is ${}".format(balance))
            else:
                print("\nPlease enter a valid number")
    # Option 3
    elif menuSelect == '3':
        print("\nBalance $ " + str(round(balance, 2)))
    # Option 4
    elif menuSelect == '4':
        print("\nThank you for Banking with us")
        running = 0
    # Invalid input response
    else:
        print("\nYou did not enter a proper number")
    
