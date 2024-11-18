class ATM:
    def __init__(self):
        self.users={"4534":{"pin":"1111","balance":1000},
                    "5687":{"pin":"2222","balance":2000},
                    "2314":{"pin":"3333","balance":1500}}
        self.logged_in=False
        self.current_user=None
    
    def login(self):
        card_number= input("Enter your card number:")
        pin=input("Enter you PIN:")
        if card_number in self.users and self.users[card_number]["pin"]==pin:
            self.logged_in=True
            self.current_user=card_number
            print("login successful!")
        else:
            print("Invalid card number or PIN.")

    def logout(self):
        self.logged_in=False
        self.current_user=None
        print("you have been logged out.")
    
    def check_balance(self):
        if self.logged_in:
            print(f"Your balance is : ${self.users[self.current_user]["balance"]}")
        else:
            print("please Login first.")

    def withdraw(self):
        if self.logged_in:
            amount= float(input("Enter the number to Withdraw: "))
            if amount > 0 and amount <= self.users[self.current_user]["balance"]:
                self.users[self.current_user]["balance"]-= amount
                print(f"Withdrawal successful. Remaining Balance: $ {self.users[self.current_user]["balance"]}")
            else:
                print("Invalid amount.")
        else:
            print("Please Login first. ")
            
    def deposit(self):
        if self.logged_in:
            amount=float(input("Enter the amount to deposit: "))
            if amount >0:
                self.users[self.current_user]["balance"] +=amount
                print(f"Deposit succcessful. New balance: $ {self.users[self.current_user]["balance"]}")
            else:
                print("Invalid amount.")
        else:
            print(" please Login first. ")

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Login")
        print("2. Logout")
        print("3. Check Balance")
        print("4. Withdraw")
        print("5. Deposit")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice= input("Enter your choice: ")
            if choice =="1":
                self.login()
            elif choice =="2":
                self.logout()
            elif choice =="3":
                self.check_balance()
            elif choice =="4":
                self.withdraw()
            elif choice =="5":
                self.deposit()
            elif choice =="6":
                print("Thank you for using our ATM.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__=="__main__":
    atm=ATM()
    atm.run()


                        

