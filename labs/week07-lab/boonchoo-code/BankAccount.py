class BankAccount:
    """A simple bank account class"""
    
    def __init__(self, account_holder, initial_balance=0): #account_holder=ชื่อผู้ถือ, initial_balance=0 ถ้าไม่ส่งยอดมา)
        self.account_holder = account_holder
        self.balance = initial_balance  #ถ้าไม่ส่งมาจะเป็น0
        self.transaction_history = []
    
    def deposit(self, amount): #ฝากเงิน
        """Method to deposit money"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive"
    
    def withdraw(self, amount): #ถอนเงิน
        """Method to withdraw money"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds"
        else:
            return "Withdrawal amount must be positive"
    
    def get_balance(self):  #ดูยอดคงเหลือ
        """Method to check balance"""
        return f"Current balance: ${self.balance}"
    
    def get_transaction_history(self):  #ดูประวัติ
        """Method to get transaction history"""
        if self.transaction_history:
            return "\n".join(self.transaction_history)
        else:
            return "No transactions yet"

# Example usage
account = BankAccount("John Doe", 1000)
print(account.get_balance())    #Current balance: $1000
print(account.deposit(500))     #Deposited $500. New balance: $1500
print(account.withdraw(200))    #Withdrew $200. New balance: $1300
print("\nTransaction History:")     #Transaction History:
print(account.get_transaction_history())    #Deposited $500
                                            #Withdrew $200