# Sample data
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
fruits = ["apple", "banana", "apple", "orange"]

# Length and counting
print(f"Length: {len(numbers)}")           # 9 ใช้บอกจำนวนสมาชิก(มีสมาชิกทั้งหมด9ตัว)
print(f"Count of 1: {numbers.count(1)}")   # 2 นับว่าในชุดข้อมูลnumbers มีเลข1กี่ตัว(มี2ตัว)
print(f"Count of apple: {fruits.count('apple')}")  # 2 นับว่าในชุดข้อมูลfruits มีappleกี่อัน(2อัน)

# Finding elements
print(f"Index of 4: {numbers.index(4)}")   # 2 คือการถามว่าในnumbersข้อมูลตัวแรกที่มีค่าเท่ากับ4 อยู่ในindexเบอร์อะไร
print(f"Index of banana: {fruits.index('banana')}")  # 1 อยู่ในindexที่1

# Sorting
numbers_copy = numbers.copy() #Sort=การจัดเรียง เรียงจากน้อยไปหามาก
numbers_copy.sort()                         # Sort in place
print(f"Sorted: {numbers_copy}")           # [1, 1, 2, 3, 4, 5, 5, 6, 9]

numbers_copy.sort(reverse=True)             # Sort descending กลับด้าน เรียงจากมากไปน้อย
print(f"Reverse sorted: {numbers_copy}")   # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# sorted() function - returns new list
sorted_numbers = sorted(numbers) #sort ไม่มีed คือ...
print(f"Original: {numbers}")              # [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"New sorted: {sorted_numbers}")     # [1, 1, 2, 3, 4, 5, 5, 6, 9]

# Reversing คือการกลับด้านลิสต์ จากตัวแรกเป็นตัวสุดท้ายเรียงมา
fruits.reverse()
print(f"Reversed fruits: {fruits}")        # ['orange', 'apple', 'banana', 'apple']

# Min, max, sum (for numeric lists)
print(f"Min: {min(numbers)}")              # 1
print(f"Max: {max(numbers)}")              # 9
print(f"Sum: {sum(numbers)}")              # 36