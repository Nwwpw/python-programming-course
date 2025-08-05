# Empty dictionary (การสร้างดิคเปล่าๆ เลือกใช้ตัวไหนก็ได้)
empty_dict = {}
another_empty_dict = dict()

# Dictionary with initial values (เก็บข้อมูลของคำ,ความหมายของมัน)
student = {
    "name": "Alice Smith",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Different data types as values
mixed_dict = {
    "string": "hello",
    "number": 42,
    "list": [1, 2, 3],
    "nested_dict": {"key": "value"},
    "boolean": True
}

# Using dict() constructor (เลือกใช้ได้เลยวิธีที่1,2เหมือนกัน)
#วิธีที่1
person = dict(name="Bob", age=25, city="Bangkok")
#วิธีที่2
person = {
    "name": "Bob",
    "age": "25",
    "city": "Bangkok"
}


# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
#(เลือกใช้ได้เลยวิธีที่1,2เหมือนกัน)
#วิธีที่1
dict_from_pairs = dict(pairs)
#วิธีที่2
dict_from_pairs = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(f"Student: {student}")
print(f"Mixed: {mixed_dict}")
print(f"Person: {person}")
print(f"From pairs: {dict_from_pairs}")