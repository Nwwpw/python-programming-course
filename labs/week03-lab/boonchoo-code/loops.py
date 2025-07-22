# Example: Print only even numbers from 1 to 10
for i in range(1, 11): #loop วน10รอบ
    if i % 2 == 0:
        print(f"{i} is even")
    else: #ถ้า=อย่างอื่นที่ไม่ใช่0 เป็นodd
        print(f"{i} is odd")
        
# Example: Input validation
password = ""
while len(password) < 8: #ต้องกรอก>8ตัว
    password = input("Enter a password (at least 8 characters): ")
    if len(password) < 8: #ถ้า<8ตัว จะประกาศว่ามันสั้นไป ลองอีกครั้ง
        print("Password too short! Try again.")
print("Password accepted!")


# Example: Multiplication table
#loop i,j วนloopละ3รอบ
for i in range(1, 4):  # rows(แนวนอน)
    for j in range(1, 4):  # columns(แนวตั้ง)
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # new line after each row
    
    
    
# Break example: Find first number divisible by 7
for num in range(1, 100): #วน99รอบ
    if num % 7 == 0: #ทำไปเรื่อยๆจนถึงnum=7เพราะถ้าไม่ถึง7จะเป็น0เศษ...)
        print(f"First number divisible by 7: {num}")
        break

# Continue example: Skip negative numbers
numbers = [5, -3, 8, -1, 12, -7, 4]
for num in numbers:
    if num < 0:
        continue  # skip negative numbers (กระโดดไปที่หัวของloopที่อยู่ใกล้กับตัวมันมากที่สุด)
    print(f"Positive number: {num}")