"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""

#A global variable passing_grade = 50
passing_grade = 50

#(1) A function input_students(num_students)
def input_students(num_students=0):
    # สร้างรายชื่อนักเรียนและคะแนน 3 วิชาในรูปแบบ list ของ dictionary
    students = [
        {
            'name': 'Manee',
            'scores': [81, 72, 98]
        },
        {'name': 'Mana', 'scores': [70, 40, 52]}
    ]
    return students

#(2) A function calculate_averages(students)
def calculate_averages(students):
    for student in students:
        sum = 0     # ตัวแปรเก็บผลรวมคะแนน
        for score in student['scores']:     # วนลูปคะแนนแต่ละวิชา
            sum = sum + score       # บวกคะแนนเข้า sum
        student['average'] = sum / len(student['scores'])       # คำนวณค่าเฉลี่ยและเพิ่มใน dictionary
    
    return students

# (3) A function display_results(students)
def display_results(students):
    for student in students:    # วนลูปแต่ละคน
        print("Name: ",student['name'])     # แสดงชื่อ
        print("Average: %.2f" % student['average'])       # แสดงค่าเฉลี่ย
        if student['average'] > passing_grade:      # เช็คว่าผ่านหรือไม่
            print("Status: PASS")
        else:
            print("Status: FAIL")

students_list = input_students()       # สร้างรายชื่อนักเรียน
students_list = calculate_averages(students_list)       # คำนวณค่าเฉลี่ย
display_results(students_list)      # แสดงผลลัพธ์