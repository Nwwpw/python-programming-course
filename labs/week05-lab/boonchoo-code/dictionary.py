# Empty dictionary
empty_dict = {}     # สร้าง dictionary ว่าง
another_empty_dict = dict()     # อีกวิธีสร้าง dictionary ว่าง

# Dictionary with initial values (Dictionary กำหนดค่าเริ่มต้น)
student = {
    "name": "Alice Smith",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Different data types as values (Dictionary ที่เก็บค่าหลากหลายประเภท)
mixed_dict = {
    "string": "hello",
    "number": 42,
    "list": [1, 2, 3],
    "nested_dict": {"key": "value"},
    "boolean": True
}

# Using dict() constructor (Dictionary ที่สร้างด้วย dict() constructor)
person = dict(name="Bob", age=25, city="Bangkok")

# From list of tuples (Dictionary จาก list ของ tuple)
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)

print(f"Student: {student}")
print(f"Mixed: {mixed_dict}")
print(f"Person: {person}")
print(f"From pairs: {dict_from_pairs}")


""""
Summ.
    {} หรือ dict() → สร้าง dictionary ว่าง

    {"key": value} → กำหนดค่าเริ่มต้น

    ค่าของ dictionary สามารถเป็นได้ทุกประเภท (string, int, list, dict, bool)

    dict(key=value, ...) → ใช้ constructor สร้าง dict

    dict(list_of_tuples) → แปลง list ของ tuple เป็น dict
"""