# Sample data
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96, "Eve": 89}

# Length and membership
print(f"Number of students: {len(scores)}") #5 (มี5จำนวนใน scores)
print(f"Is Alice in scores? {'Alice' in scores}") #True (มีAliceอยู่ใน scoresไหม มีเลยตอบTrue)
print(f"Is 'Frank' in scores? {'Frank' in scores}") #False (มีFrankอยู่ใน scoresไหม ไม่มีเลยตอบFalse)

# Getting keys, values, items
print(f"Students: {list(scores.keys())}") #['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
print(f"Scores: {list(scores.values())}") #[85, 92, 78, 96, 89]
print(f"All data: {list(scores.items())}") #[('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 96), ('Eve', 89)]

# Iterating through dictionary
print("\nAll students and scores:")
for name, score in scores.items():
    print(f"{name}: {score}")

print("\nJust the names:")
for name in scores.keys():
    print(name)

print("\nJust the scores:")
for score in scores.values():
    print(score)

# Dictionary comprehension for filtering
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(f"High scores (>=90): {high_scores}") #High scores (>=90): {'Bob': 92, 'Diana': 96}

# Finding min/max
best_student = max(scores, key=scores.get)
worst_student = min(scores, key=scores.get)
print(f"Best student: {best_student} with {scores[best_student]}") #Diana with 96
print(f"Lowest score: {worst_student} with {scores[worst_student]}") #Lowest score: Charlie with 78

# fromkeys() method (พยายามสร้างdictจากkey=subjects)
subjects = ["Math", "Science", "English"]
default_scores = dict.fromkeys(subjects, 0) #สร้างdictจากkey=subjectsที่มีค่าเริ่มต้นเป็น0
print(f"Default scores: {default_scores}") #Default scores: {'Math': 0, 'Science': 0, 'English': 0}

# setdefault() method
student_grades = {}
student_grades.setdefault("Alice", []).append(85)
student_grades.setdefault("Alice", []).append(92)
student_grades.setdefault("Bob", []).append(78)
print(f"Student grades: {student_grades}") #Student grades: {'Alice': [85, 92], 'Bob': [78]}