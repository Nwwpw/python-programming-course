# Sample data (กำหนดคะแนนนักเรียนเป็น dictionary)
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96, "Eve": 89}

<<<<<<< HEAD
# Length and membership
print(f"Number of students: {len(scores)}") #5 (มี5จำนวนใน scores)
print(f"Is Alice in scores? {'Alice' in scores}") #True (มีAliceอยู่ใน scoresไหม มีเลยตอบTrue)
print(f"Is 'Frank' in scores? {'Frank' in scores}") #False (มีFrankอยู่ใน scoresไหม ไม่มีเลยตอบFalse)

# Getting keys, values, items
print(f"Students: {list(scores.keys())}") #['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
print(f"Scores: {list(scores.values())}") #[85, 92, 78, 96, 89]
print(f"All data: {list(scores.items())}") #[('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 96), ('Eve', 89)]
=======
# Length and membership (นับจำนวนสมาชิกและเช็คว่ามี key อยู่ใน dictionary ไหม)
print(f"Number of students: {len(scores)}") #5 (จำนวน students)
print(f"Is Alice in scores? {'Alice' in scores}") #True (เช็คว่ามี 'Alice' เป็น key ไหม)
print(f"Is 'Frank' in scores? {'Frank' in scores}") #False (เช็ค 'Frank' ด้วย)

# Getting keys, values, items (ดึง key, value, items(key+values))
print(f"Students: {list(scores.keys())}") #Students: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'] (key)
print(f"Scores: {list(scores.values())}") #Scores: [85, 92, 78, 96, 89] (value)
print(f"All data: {list(scores.items())}") #All data: [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 96), ('Eve', 89)] (key+value)
>>>>>>> c7f5e05d71b6af52a40ead7b011b2d7d23a323e1

# Iterating through dictionary (วนลูปดูข้อมูลทั้งหมด)
print("\nAll students and scores:")
for name, score in scores.items(): #.items() ให้ทั้ง key และ value
    print(f"{name}: {score}") 
    """""
    Alice: 85
    Bob: 92
    Charlie: 78
    Diana: 96
    Eve: 89
    """""

print("\nJust the names:")
for name in scores.keys(): #.keys() ให้เฉพาะ key
    print(name)
    """""
    Alice
    Bob
    Charlie
    Diana
    Eve
    """""

print("\nJust the scores:")
for score in scores.values(): #.values() ให้เฉพาะ value
    print(score)
    """""
    85
    92
    78
    96
    89
    """""

# Dictionary comprehension for filtering (สร้าง dict ใหม่โดยกรองค่า)
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(f"High scores (>=90): {high_scores}") #High scores (>=90): {'Bob': 92, 'Diana': 96}

# Finding min/max (หาค่า max/min ของ dictionary โดยใช้ key)
best_student = max(scores, key=scores.get)
worst_student = min(scores, key=scores.get)
<<<<<<< HEAD
print(f"Best student: {best_student} with {scores[best_student]}") #Diana with 96
print(f"Lowest score: {worst_student} with {scores[worst_student]}") #Lowest score: Charlie with 78

# fromkeys() method (พยายามสร้างdictจากkey=subjects)
subjects = ["Math", "Science", "English"]
default_scores = dict.fromkeys(subjects, 0) #สร้างdictจากkey=subjectsที่มีค่าเริ่มต้นเป็น0
=======
print(f"Best student: {best_student} with {scores[best_student]}") #Best student: Diana with 96
print(f"Lowest score: {worst_student} with {scores[worst_student]}") #Lowest score: Charlie with 78

# fromkeys() method (สร้าง dictionary ใหม่จาก list ของ key พร้อมค่า default)
subjects = ["Math", "Science", "English"]
default_scores = dict.fromkeys(subjects, 0)
>>>>>>> c7f5e05d71b6af52a40ead7b011b2d7d23a323e1
print(f"Default scores: {default_scores}") #Default scores: {'Math': 0, 'Science': 0, 'English': 0}

# setdefault() method (เพิ่มค่าใน dictionary แบบ list ถ้า key ยังไม่มีจะสร้างให้)
student_grades = {}
student_grades.setdefault("Alice", []).append(85) #ถ้า 'Alice' ไม่มี จะสร้าง list ให้ก่อน
student_grades.setdefault("Alice", []).append(92) #เพิ่ม 92 เข้า list ของ Alice
student_grades.setdefault("Bob", []).append(78)
<<<<<<< HEAD
print(f"Student grades: {student_grades}") #Student grades: {'Alice': [85, 92], 'Bob': [78]}
=======
print(f"Student grades: {student_grades}") #Student grades: {'Alice': [85, 92], 'Bob': [78]}



""""
Summ.
    len(dict) → นับจำนวน key

    'key' in dict → เช็ค key มีไหม

    dict.keys(), dict.values(), dict.items() → ดึง key / value / ทั้งคู่

    for k, v in dict.items() → วนดูทั้งคู่

    {k:v for k,v in dict.items() if ...} → กรองข้อมูลง่าย ๆ

    max(dict, key=dict.get) → หาค่า max ตาม value

    dict.fromkeys(list, default) → สร้าง dict ใหม่พร้อมค่าเริ่มต้น

    dict.setdefault(key, default) → เพิ่มค่าโดยไม่ต้องเช็คว่ามี key หรือยัง
"""
>>>>>>> c7f5e05d71b6af52a40ead7b011b2d7d23a323e1
