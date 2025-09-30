"""1. Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance. (สร้างคลาส BankAccount พร้อม attribute)"""

class BankAccount:
    """2. Create a constructor with parameters: accountNumber, name, balance. (สร้าง constructor รับ accountNumber, name, balance)"""
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber  # หมายเลขบัญชี (numeric)
        self.name = name                    # ชื่อเจ้าของบัญชี (string)
        self.balance = balance              # ยอดเงินคงเหลือ (numeric)

    """3. Create a Deposit() method which manages the deposit actions. (สร้างเมธอด Deposit สำหรับฝากเงิน)"""
    def Deposit(self, amount):      # ฝากเงินเข้าบัญชี
        self.balance += amount

    """4. Create a Withdrawal() method which manages withdrawals actions. (สร้างเมธอด Withdrawal สำหรับถอนเงิน)"""
    def Withdrawal(self, amount):       # ถอนเงินออกจากบัญชี ถ้ายอดเงินพอ
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    """5. Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account. (สร้างเมธอด bankFees สำหรับหักค่าธรรมเนียม 5%)"""
    def bankFees(self):     # หักค่าธรรมเนียม 5% ของยอดเงินคงเหลือ
        self.balance -= self.balance * 0.05

    """6. Create a display() method to display account details. (สร้างเมธอด display สำหรับแสดงรายละเอียดบัญชี)"""
    def display(self):      # แสดงรายละเอียดบัญชี
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Name: {self.name}")
        print(f"Balance: {self.balance:.2f}")


"""test"""
# สร้างบัญชีใหม่
account = BankAccount(888888, "Namwan", 1000)

# แสดงรายละเอียดบัญชี
print("== Display account details ==")
account.display()

# ฝากเงิน
print("\n== ฝากเงิน 500 บาท ==")
account.Deposit(500)
account.display()

# ถอนเงิน
print("\n== Withdraw 300 baht ==")
if account.Withdrawal(300):
    print("Withdrawal successful")
else:
    print("Insufficient funds")
account.display()

# ถอนเงินเกินยอด
print("\n== Withdraw 2000 baht ==")
if account.Withdrawal(2000):
    print("Withdrawal successful")
else:
    print("Insufficient funds") #ยอดเงินไม่พอ
account.display()

# หักค่าธรรมเนียม 5%
print("\n== Deduct 5% bank fee ==") #หักค่าธรรมเนียม 5%
account.bankFees()
account.display()