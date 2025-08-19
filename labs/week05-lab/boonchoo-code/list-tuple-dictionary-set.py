# Use DICTIONARIES when: (ใช้ DICTIONARIES เมื่อ:)
# 1. You need key-value relationships (ต้องการเก็บความสัมพันธ์แบบ key-value)
student_info = {
    "id": "12345",
    "name": "Alice",
    "courses": ["Python", "Math"],
    "gpa": 3.8
}

# 2. Fast lookups by key (ต้องการค้นหาข้อมูลโดยใช้ key ได้เร็ว)
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

# 3. Counting occurrences (นับจำนวนครั้งที่คำปรากฏ)
text = "hello world hello python"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1      # ใช้ get() ถ้า key ไม่มีจะได้ 0
print(f"Word count: {word_count}")      # แสดงผลการนับคำ

# Use SETS when: (ใช้ SETS เมื่อ:)
# 1. You need unique elements (ต้องการเก็บค่าไม่ซ้ำ)
email_subscribers = {"alice@email.com", "bob@email.com", "charlie@email.com"}
email_subscribers.add("alice@email.com")  # Won't add duplicate(ไม่เพิ่มค่าซ้ำ)
print(f"Unique subscribers: {email_subscribers}")

# 2. Mathematical set operations (ทำ operation แบบเซตทางคณิตศาสตร์)
active_users = {"user1", "user2", "user3", "user4"}
premium_users = {"user2", "user4", "user5"}
active_premium = active_users & premium_users       # ตัด intersection
print(f"Active premium users: {active_premium}")

# 3. Fast membership testing (ตรวจสอบการเป็นสมาชิกได้เร็ว)
valid_codes = {"A001", "B002", "C003", "D004"}
user_code = "B002"
if user_code in valid_codes:  # O(1) average time(ตรวจสอบ membership O(1) โดยเฉลี่ย)
    print("Valid code!")

# 4. Removing duplicates from lists (ลบค่าซ้ำใน list)
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = list(set(numbers_with_duplicates))     # แปลงเป็น set แล้วกลับเป็น list
print(f"Unique numbers: {unique_numbers}")


""""
Summ.
    Dictionary → เก็บข้อมูลแบบ key-value, ค้นหาด้วย key, นับจำนวน, map ข้อมูล
    Set → เก็บค่าที่ไม่ซ้ำ, operation แบบเซต (union, intersection), ตรวจสอบ membership, ลบ duplicate จาก list
"""