# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance") #เช็คยอดเงิน
        print("2. Withdraw") #ถามว่าถอนเท่าไหร่(หักออกจากยอดเดิม)
        print("3. Deposit") #ต้องการฝากเงินเท่าไหร่(เอาไปบวกยอดเดิม)
        print("4. Exit") #break
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "4": #อย่าลืมใส่""ที่เลข
            break

        elif choice == "3":
            deposit = float(input("Deposit amount: ")) #เพิ่มป้องกันฝากยอดติดลบ
            if deposit < 0:
                print("Can't deposit less than 0")
                continue
            else:
                balance = balance + deposit
                print("Successfully, Your balance now = ", balance)

        elif choice == "2": #เพิ่มป้องกันห้ามถอนเงินติดลบ,เกินยอดที่มี
            withdraw = float(input("Withdraw amount: ")) #เพิ่มป้องกันฝากยอดติดลบ
            if withdraw < 0:
                print("Can't withdraw less than 0")
                continue
            elif withdraw > balance:
                print("Can't withdraw more than balance")
                continue
            else:
                balance = balance - withdraw
                print("Successfully, Your balance now = ", balance)

        elif choice == "1":
            print("Your balance now = ", balance)
            continue

else:
    print("Invalid PIN")