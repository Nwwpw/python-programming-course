# Empty set (note: {} creates empty dict, not set) (note: {} สร้าง dict ว่าง ไม่ใช่ set)
empty_set = set()

# Set with initial values
colors = {"red", "green", "blue", "yellow"}
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}

# Set from list (removes duplicates) (ลบค่าซ้ำอัตโนมัติ)
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(list_with_duplicates)      # แปลงเป็น set → เหลือค่าที่ไม่ซ้ำ
print(f"Original list: {list_with_duplicates}")
print(f"Set (unique): {unique_numbers}")

# Set from string (สร้าง set จาก string)
char_set = set("hello")     # แยกตัวอักษรใน string
print(f"Characters in 'hello': {char_set}")

# Set comprehension
squares = {x**2 for x in range(1, 6)}       # สร้าง set ของกำลังสอง
print(f"Squares: {squares}")

print(f"Colors: {colors}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed_set}")


""""
Summ.
    set() → สร้าง set ว่าง

    {value1, value2} → สร้าง set พร้อมค่า

    set(list) → ลบค่าซ้ำจาก list

    set(string) → แยกตัวอักษรเป็น set

    {x for x in iterable} → set comprehension, สร้าง set แบบ loop
"""