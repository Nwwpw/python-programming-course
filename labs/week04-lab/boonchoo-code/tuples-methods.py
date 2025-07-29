numbers = (1, 2, 3, 2, 4, 2, 5)
colors = ("red", "green", "blue")

# Length
print(f"Length: {len(numbers)}")         # 7 (นับจำนวนสมาชิก)

# Count occurrences
print(f"Count of 2: {numbers.count(2)}") # 3 (นับว่าเลข2มีกี่ตัว มี3ตัว)

# Find index
print(f"Index of 3: {numbers.index(3)}")  # 2 (indexที่3 คือ 2)

# Check membership
print(f"Is 'red' in colors? {'red' in colors}")      # True หาว่ามีredไหม มีเลยตอบTrue
print(f"Is 'yellow' in colors? {'yellow' in colors}") # False หาว่ามีyellowไหม ไม่มีเลยตอบFalse

# Min, max, sum (for numeric tuples)
print(f"Min: {min(numbers)}")            # 1
print(f"Max: {max(numbers)}")            # 5
print(f"Sum: {sum(numbers)}")            # 19

# Converting to list and back
numbers_list = list(numbers)
print(f"As list: {numbers_list}")
new_tuple = tuple(numbers_list)
print(f"Back to tuple: {new_tuple}")

# Concatenation and repetition
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2 #เอามาต่อกัน
print(f"Combined: {combined}")           # (1, 2, 3, 4, 5, 6)

repeated = tuple1 * 3 #คือการเอาtupleมาต่อกัน3รอบ
print(f"Repeated: {repeated}")           # (1, 2, 3, 1, 2, 3, 1, 2, 3)