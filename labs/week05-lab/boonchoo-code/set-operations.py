# Basic set operations (ตัวอย่างการใช้งาน set เบื้องต้น)
fruits = {"apple", "banana", "orange", "grape"}
citrus = {"orange", "lemon", "lime", "grapefruit"}

print(f"Fruits: {fruits}")
print(f"Citrus: {citrus}")

# Adding elements (เพิ่ม element เดียว)
fruits.add("strawberry")
print(f"After adding strawberry: {fruits}")

# Adding multiple elements (เพิ่มหลาย element)
fruits.update(["kiwi", "mango"])
print(f"After adding multiple: {fruits}")

# Removing elements (ลบ element)
fruits.remove("banana")  # Raises error if not found (ถ้าไม่เจอจะ error)
print(f"After removing banana: {fruits}")

fruits.discard("pineapple")  # No error if not found
print(f"After discarding pineapple: {fruits}")

removed_fruit = fruits.pop()  # Remove arbitrary element (ลบ element แบบสุ่ม)
print(f"Removed: {removed_fruit}")
print(f"Remaining fruits: {fruits}")

# Set mathematical operations (การทำ operation แบบเซต)
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union (all elements from both sets) (รวมทุก element ของทั้งสอง set)
union = set_a | set_b  # or set_a.union(set_b)      # หรือ set_a.union(set_b)
print(f"Union (A | B): {union}")

# Intersection (common elements) (element ที่มีเหมือนกันในทั้งสอง set)
intersection = set_a & set_b  # or set_a.intersection(set_b)        # หรือ set_a.intersection(set_b)
print(f"Intersection (A & B): {intersection}")

# Difference (elements in A but not in B) (element ที่อยู่ใน A แต่ไม่อยู่ใน B)
difference = set_a - set_b  # or set_a.difference(set_b) (หรือ set_a.difference(set_b))
print(f"Difference (A - B): {difference}")

# Symmetric difference (elements in either A or B, but not both) (element ที่อยู่ใน A หรือ B แต่ไม่อยู่ทั้งสอง)
sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)        # หรือ set_a.symmetric_difference(set_b)
print(f"Symmetric difference (A ^ B): {sym_diff}")


""""
Summ.
    .add() → เพิ่ม element เดียว

    .update() → เพิ่มหลาย element

    .remove() → ลบ element (error ถ้าไม่มี)

    .discard() → ลบ element (ไม่ error ถ้าไม่มี)

    .pop() → ลบ element แบบสุ่ม

    | หรือ .union() → union

    & หรือ .intersection() → intersection

    - หรือ .difference() → difference

    ^ หรือ .symmetric_difference() → symmetric difference
"""