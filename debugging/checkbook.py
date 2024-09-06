#!/usr/bin/python3
class Checkbook:
    """
    A simple Checkbook class that allows users to deposit, withdraw, and check their balance.

    Attributes:
    balance (float): The current balance of the checkbook, initialized to 0.0.
    """
    
    def __init__(self):
        """
        Initializes the Checkbook class with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a given amount into the checkbook and updates the balance.

        Parameters:
        amount (float): The amount to deposit. Must be positive.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a given amount from the checkbook if sufficient funds are available.

        Parameters:
        amount (float): The amount to withdraw. Must be positive and less than or equal to the current balance.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    The main function that interacts with the user and allows them to deposit, withdraw, check balance, or exit.
    
    Handles invalid input and prompts the user for valid actions and numeric values.

    Returns:
    None
    """
    cb = Checkbook()  # Create an instance of the Checkbook class
    while True:
        # Prompt user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        
        if action == 'exit':
            # Exit the program
            break
        elif action == 'deposit':
            try:
                # Get deposit amount from the user
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    # Ensure deposit amount is positive
                    print("Please enter a positive amount.")
                else:
                    cb.deposit(amount)
            except ValueError:
                # Handle non-numeric input
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                # Get withdrawal amount from the user
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    # Ensure withdrawal amount is positive
                    print("Please enter a positive amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                # Handle non-numeric input
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            # Print the current balance
            cb.get_balance()
        else:
            # Handle invalid commands
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
