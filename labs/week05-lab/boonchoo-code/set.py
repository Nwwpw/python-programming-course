# Empty set (note: {} creates empty dict, not set)
empty_set = set()

# Set with initial values
colors = {"red", "green", "blue", "yellow"}
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}

# Set from list (removes duplicates)
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(list_with_duplicates)
print(f"Original list: {list_with_duplicates}") #[1, 2, 2, 3, 3, 3, 4, 5]
print(f"Set (unique): {unique_numbers}") #{1, 2, 3, 4, 5} (ลบตัวที่ซ้ำออก เหลือ1ตัว)

# Set from string
char_set = set("hello") #{'o', 'e', 'h', 'l'}
char_list = list("hello") # ['h','e','l','l','o'] >>เพิ่มบรรทัดนี้มาเอง ให้เข้าใจมากขึ้นเฉยๆ
chartuple = tuple("hello") # ('h','e','l','l','o') >>เพิ่มบรรทัดนี้มาเอง ให้เข้าใจมากขึ้นเฉยๆ
print(f"Characters in 'hello': {char_set}") #{'o', 'e', 'h', 'l'} (ลบตัวที่ซ้ำออก เหลือ1ตัว)

# Set comprehension
squares = {x**2 for x in range(1, 6)} #(6-1=วน5รอบ) ตั้งแต่1-5 ค่อยๆยกกำลัง2ไปทีละตัว
print(f"Squares: {squares}") #{1, 4, 9, 16, 25}

print(f"Colors: {colors}") #{'green', 'yellow', 'red', 'blue'}
print(f"Numbers: {numbers}") #{1, 2, 3, 4, 5}
print(f"Mixed: {mixed_set}") #{1, 3.14, 'hello'}