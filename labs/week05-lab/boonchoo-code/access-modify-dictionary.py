student = {
    "name": "Alice Smith",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": ["Python", "Java", "Calculus"] # เก็บรายวิชาในรูปแบบ list
}
#พวกname, ageคือkey / พวกAlice Smith, 20คือvalue

# Accessing values by key (ดึงค่าจาก key โดยตรง)
print(f"Name: {student['name']}")           # Alice Smith
print(f"Age: {student['age']}")             # 20

# Using get() method (safer) > ใช้get() ปลอดภัยกว่า ถ้าkeyไม่มีจะขึ้นerror
print(f"Major: {student.get('major')}")     # Computer Science
<<<<<<< HEAD
print(f"Phone: {student.get('phone')}")     # None (key doesn't exist)->ไม่มีkeyที่ชื่อphone
print(f"Phone: {student.get('phone', 'Not provided')}")  # Default value
=======
print(f"Phone: {student.get('phone')}")     # None (key doesn't exist) ได้None(ไม่มีkey)
print(f"Phone: {student.get('phone', 'Not provided')}")  # Default value กำหนดค่าDefaultเองได้
>>>>>>> c7f5e05d71b6af52a40ead7b011b2d7d23a323e1

# Accessing nested data เข้าถึงข้อมูลที่ซ้อนอยู่ (list ใน dict)
print(f"First course: {student['courses'][0]}")  # Python แสดงวิชาแรก

# Check if key exists ตรวจสอบว่ามี key อยู่หรือไม่
if 'gpa' in student:
    print(f"GPA: {student['gpa']}")

# Get all keys, values, and items ดึง key, value, item ทั้งหมด
print(f"Keys: {list(student.keys())}") #['name', 'age', 'major', 'gpa', 'courses'] (รายชื่อ key)
print(f"Values: {list(student.values())}") #['Alice Smith', 20, 'Computer Science', 3.8, ['Python', 'Java', 'Calculus']] (รายชื่อค่า)
print(f"Items: {list(student.items())}") #[('name', 'Alice Smith'), ('age', 20), ('major', 'Computer Science'), ('gpa', 3.8), ('courses', ['Python', 'Java', 'Calculus'])] (key + value)


<<<<<<< HEAD
""" modify dictionary """ #modify=แก้
=======
""" modify dictionary """ #ปรับแต่ง dictionary
>>>>>>> c7f5e05d71b6af52a40ead7b011b2d7d23a323e1


# Creating a dictionary
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

print(f"Original inventory: {inventory}") #{'apples': 50, 'bananas': 30, 'oranges': 25}

# Adding new items (ทีแรกไม่มีองุ่น,สตอ เลยเพิ่มข้อมูลเข้าไปจากที่key=3->key=5)
inventory["grapes"] = 40
inventory["strawberries"] = 15
print(f"After adding items: {inventory}") #{'apples': 50, 'bananas': 30, 'oranges': 25, 'grapes': 40, 'strawberries': 15}       

<<<<<<< HEAD
# Updating existing items (แก้จำนวนapple=25,เพิ่มbananaไปอีก20)
inventory["apples"] = 45  # Reduce apple count
inventory["bananas"] += 20  # Add more bananas
print(f"After updates: {inventory}")

# Using update() method (เหมือน44-47 องุ่น,สตอ)
=======
# Updating existing items (อัปเดตค่าที่มีอยู่แล้ว)
inventory["apples"] = 45  # Reduce apple count (กำหนดค่าใหม่ตรง ๆ)
inventory["bananas"] += 20  # Add more bananas (ใช้ค่าเดิมแล้วบวกเพิ่ม)
print(f"After updates: {inventory}") #{'apples': 45, 'bananas': 50, 'oranges': 25, 'grapes': 40, 'strawberries': 15}

# Using update() method (อัปเดตหลายค่าในครั้งเดียว ด้วย update())
>>>>>>> c7f5e05d71b6af52a40ead7b011b2d7d23a323e1
new_items = {"mangoes": 35, "pineapples": 10}
inventory.update(new_items)
print(f"After bulk update: {inventory}") #{'apples': 45, 'bananas': 50, 'oranges': 25, 'grapes': 40, 'strawberries': 15, 'mangoes': 35, 'pineapples': 10}

# Update with another syntax (อัปเดตด้วย keyword argument (เขียนสั้นกว่า))
inventory.update(apples=60, bananas=55)
print(f"After keyword update: {inventory}") #{'apples': 60, 'bananas': 55, 'oranges': 25, 'grapes': 40, 'strawberries': 15, 'mangoes': 35, 'pineapples': 10}

<<<<<<< HEAD
# Removing items (ลบ แต่มีการเอาข้อมูลมาทำงานต่อทีหลัง.)
removed_item = inventory.pop("strawberries")  # Remove and return value
print(f"Removed {removed_item} strawberries")

del inventory["pineapples"]  # Remove without returning (ดีดpineapplesออกใช้methodชื่อdel)(ลบ ไม่มีการเอาข้อมูลมาทำงานต่อทีหลัง.)
print(f"After deletions: {inventory}")
=======
# Removing items
removed_item = inventory.pop("strawberries")  # Remove and return value (pop คืนค่าที่ถูกลบด้วย)
print(f"Removed {removed_item} strawberries") #Removed 15 strawberries

del inventory["pineapples"]  # Remove without returning (# del ไม่คืนค่า)
print(f"After deletions: {inventory}") #After deletions: {'apples': 60, 'bananas': 55, 'oranges': 25, 'grapes': 40, 'mangoes': 35}
>>>>>>> c7f5e05d71b6af52a40ead7b011b2d7d23a323e1

# Remove last item (Python 3.7+) (ลบ item สุดท้ายที่ถูกเพิ่ม (Python 3.7+))
last_item = inventory.popitem()
print(f"Last item removed: {last_item}") #Last item removed: ('mangoes', 35)

# Clear all items (เคลียร์ dictionary ทั้งหมด)
backup = inventory.copy() #สำรองไว้ก่อน
inventory.clear()
print(f"After clear: {inventory}") #After clear: {}
print(f"Backup: {backup}") #Backup: {'apples': 60, 'bananas': 55, 'oranges': 25, 'grapes': 40}