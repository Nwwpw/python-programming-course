# Basic set operations
fruits = {"apple", "banana", "orange", "grape"}
citrus = {"orange", "lemon", "lime", "grapefruit"}

print(f"Fruits: {fruits}") #{'grape', 'apple', 'orange', 'banana'}
print(f"Citrus: {citrus}") #{'grapefruit', 'lime', 'orange', 'lemon'}

# Adding elements
fruits.add("strawberry")
print(f"After adding strawberry: {fruits}") #{'apple', 'banana', 'strawberry', 'orange', 'grape'}

# Adding multiple elements
fruits.update(["kiwi", "mango"])
print(f"After adding multiple: {fruits}") #{'apple', 'kiwi', 'banana', 'strawberry', 'orange', 'grape', 'mango'}

# Removing elements
fruits.remove("banana")  # Raises error if not found
print(f"After removing banana: {fruits}") #{'apple', 'kiwi', 'strawberry', 'orange', 'grape', 'mango'}

fruits.discard("pineapple")  # No error if not found (เอาpineappleออก แต่ไม่มีpineappleเลยเหมือนเดิม)
print(f"After discarding pineapple: {fruits}") #{'apple', 'kiwi', 'strawberry', 'orange', 'grape', 'mango'}

removed_fruit = fruits.pop()  # Remove arbitrary element (popต้องมีitemมารองรับเสมอ)
print(f"Removed: {removed_fruit}") #Removed: apple
print(f"Remaining fruits: {fruits}") #Remaining fruits: {'kiwi', 'strawberry', 'orange', 'grape', 'mango'}

# Set mathematical operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}") #Set A: {1, 2, 3, 4, 5}
print(f"Set B: {set_b}") #Set B: {4, 5, 6, 7, 8}

# Union (all elements from both sets)
union = set_a | set_b  # or set_a.union(set_b)
print(f"Union (A | B): {union}") #Union (A | B): {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (common elements)
intersection = set_a & set_b  # or set_a.intersection(set_b)
print(f"Intersection (A & B): {intersection}") #Intersection (A & B): {4, 5}

# Difference (elements in A but not in B)
difference = set_a - set_b  # or set_a.difference(set_b)
print(f"Difference (A - B): {difference}") #Difference (A - B): {1, 2, 3}

# Symmetric difference (elements in either A or B, but not both)
sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(f"Symmetric difference (A ^ B): {sym_diff}") #Symmetric difference (A ^ B): {1, 2, 3, 6, 7, 8}