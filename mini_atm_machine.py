class BankAccount:
    """Represents a bank account with secure operations"""
    
    def __init__(self, account_number, pin, balance=0): 
        """Initialize a new bank account"""
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance
        self.__transaction_history = []
        self.__add_transaction("Account created", balance)
    
    def validate_pin(self, entered_pin):
        """Validate the entered PIN"""
        return self.__pin == entered_pin
    
    def check_balance(self):
        """Display current account balance"""
        print(f"\n Current Balance: ${self.__balance:.2f}")
        return self.__balance
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.__balance += amount
            self.__add_transaction("Deposit", amount)
            print(f"X Deposited: ${amount:.2f}")
            print(f"X New Balance: ${self.__balance:.2f}")
            return True
        else:
            print("X Invalid deposit amount. Must be greater than $0.")
            return False
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        # Added minimum withdrawal check
        if amount <= 0:
            print("X Invalid withdrawal amount. Must be greater than $0.")
            return False
        elif amount > self.__balance:
            print(f"X Insufficient funds. Available balance: ${self.__balance:.2f}")
            return False
        elif amount > 1000:  # Maximum withdrawal limit
            print("X Withdrawal limit exceeded. Maximum: $1000 per transaction.")
            return False
        else:
            self.__balance -= amount
            self.__add_transaction("Withdrawal", -amount)
            print(f"Withdrew: ${amount:.2f}")
            print(f"New Balance: ${self.__balance:.2f}")
            return True
    
    def change_pin(self, old_pin, new_pin):
        """Change account PIN with validation"""
        if not self.validate_pin(old_pin):
            print("X Incorrect old PIN.")
            return False
        elif len(new_pin) != 4:
            print("X New PIN must be exactly 4 digits.")
            return False
        elif not new_pin.isdigit():
            print("X New PIN must contain only numbers.")
            return False
        elif new_pin == old_pin:
            print("X New PIN must be different from old PIN.")
            return False
        else:
            self.__pin = new_pin
            self.__add_transaction("PIN changed", 0)
            print("PIN successfully changed.")
            return True
    
    def view_transaction_history(self, limit=5):
        """Display recent transaction history"""
        print(f"\n Transaction History (Last {min(limit, len(self.__transaction_history))} transactions):")
        print("-" * 60)
        
        if not self.__transaction_history:
            print("No transactions yet.")
            return
        
        # Show most recent transactions first
        recent = self.__transaction_history[-limit:][::-1]
        for transaction in recent:
            print(f"  {transaction}")
        print("-" * 60)
    
    def __add_transaction(self, transaction_type, amount):
        """Private method to add transaction to history"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if amount >= 0:
            self.__transaction_history.append(
                f"{timestamp} | {transaction_type}: +${amount:.2f}"
            )
        else:
            self.__transaction_history.append(
                f"{timestamp} | {transaction_type}: ${amount:.2f}"
            )


class ATM:
    """ATM Machine with account management"""
    
    def __init__(self):
        """Initialize ATM with empty account database"""
        self.accounts = {}
    
    def create_account(self):
        """Create a new bank account"""
        print("\n" + "=" * 60)
        print("CREATE NEW ACCOUNT")
        print("=" * 60)
        
        account_number = input("Enter new account number: ").strip()
        
        # Check for empty input
        if not account_number:
            print("X Account number cannot be empty.")
            return
        
        # Check if account already exists (FIXED: added this check)
        if account_number in self.accounts:
            print("X Account number already exists. Please choose a different one.")
            return
        
        pin = input("Set a 4-digit PIN: ").strip()
        
        # Validate PIN format
        if len(pin) != 4:
            print("X PIN must be exactly 4 digits.")
            return
        if not pin.isdigit():
            print("X PIN must contain only numbers.")
            return
        
        # Ask for initial deposit (FIXED: added initial balance option)
        while True:
            initial_balance = input("Enter initial deposit amount (minimum $0): $").strip()
            try:
                balance = float(initial_balance)
                if balance < 0:
                    print("X Initial deposit cannot be negative.")
                    continue
                break
            except ValueError:
                print("X Invalid amount. Please enter a valid number.")
        
        # Create the account
        self.accounts[account_number] = BankAccount(account_number, pin, balance)
        print(f"X Account created successfully!")
        print(f"   Account Number: {account_number}")
        print(f"   Initial Balance: ${balance:.2f}")
    
    def authenticate_account(self):
        """Authenticate user and access account"""
        print("\n" + "=" * 60)
        print("ACCOUNT LOGIN")
        print("=" * 60)
        
        account_number = input("Enter account number: ").strip()
        
        # Check if account exists
        if account_number not in self.accounts:
            print("X Account not found.")
            return
        
        # Maximum 3 PIN attempts
        max_attempts = 3
        for attempt in range(max_attempts):
            pin = input(f"Enter PIN (Attempt {attempt + 1}/{max_attempts}): ").strip()
            account = self.accounts[account_number]
            
            if account.validate_pin(pin):
                print("Authentication successful!")
                self.account_menu(account)
                return
            else:
                remaining = max_attempts - attempt - 1
                if remaining > 0:
                    print(f"X Incorrect PIN. {remaining} attempt(s) remaining.")
                else:
                    print("X Maximum attempts exceeded. Account locked.")
                    return
    
    def account_menu(self, account):
        """Display account menu with operations"""
        while True:
            print("\n" + "=" * 60)
            print("ATM MENU")
            print("=" * 60)
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Transaction History")
            print("5. Change PIN")
            print("6. Logout")
            print("=" * 60)
            
            choice = input("Choose an option (1-6): ").strip()
            
            if choice == '1':
                account.check_balance()
            
            elif choice == '2':
                amount_str = input("Enter deposit amount: $").strip()
                try:
                    amount = float(amount_str)
                    account.deposit(amount)
                except ValueError:
                    print("X Invalid amount. Please enter a valid number.")
            
            elif choice == '3':
                amount_str = input("Enter withdrawal amount: $").strip()
                try:
                    amount = float(amount_str)
                    account.withdraw(amount)
                except ValueError:
                    print("X Invalid amount. Please enter a valid number.")
            
            elif choice == '4':
                try:
                    limit = input("How many transactions to show? (default 5): ").strip()
                    limit = int(limit) if limit else 5
                    account.view_transaction_history(limit)
                except ValueError:
                    account.view_transaction_history()
            
            elif choice == '5':
                old_pin = input("Enter old PIN: ").strip()
                new_pin = input("Enter new 4-digit PIN: ").strip()
                account.change_pin(old_pin, new_pin)
            
            elif choice == '6':
                print("Logged out successfully.")
                break
            
            else:
                print("X Invalid option. Please choose 1-6.")


def main_menu():
    """Main menu for ATM system"""
    atm = ATM()
    
    print("\n" + "=" * 60)
    print("WELCOME TO MINI ATM MACHINE")
    print("=" * 60)
    
    while True:
        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print("1. Create New Account")
        print("2. Access Existing Account")
        print("3. Exit")
        print("=" * 60)
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            atm.create_account()
        
        elif choice == '2':
            atm.authenticate_account()
        
        elif choice == '3':
            print("\n" + "=" * 60)
            print("Thank you for using Mini ATM Machine!")
            print("Have a great day!")
            print("=" * 60)
            break
        
        else:
            print("X Invalid option. Please choose 1-3.")


# Start the ATM Machine
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        print("Goodbye!")
    except Exception as e:
        print(f"\nX An unexpected error occurred: {e}")
        print("Please restart the program.")