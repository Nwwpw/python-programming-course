# Set relationships(ความสัมพันธ์ระหว่าง set)
all_animals = {"dog", "cat", "bird", "fish", "rabbit", "hamster"}
pets = {"dog", "cat", "rabbit"}
mammals = {"dog", "cat", "rabbit", "hamster"}
small_pets = {"cat", "rabbit", "hamster"}

print(f"All animals: {all_animals}")
print(f"Pets: {pets}")
print(f"Mammals: {mammals}")
print(f"Small pets: {small_pets}")

# Subset and superset (ตรวจสอบ subset / superset)
print(f"Are pets subset of all animals? {pets.issubset(all_animals)}")
print(f"Are all animals superset of pets? {all_animals.issuperset(pets)}")

# Disjoint sets (no common elements) (ไม่มี element ร่วมกัน)
birds = {"eagle", "sparrow", "parrot"}
print(f"Birds: {birds}")
print(f"Are mammals and birds disjoint? {mammals.isdisjoint(birds)}")
print(f"Are pets and small_pets disjoint? {pets.isdisjoint(small_pets)}")

# Set equality (ตรวจสอบความเท่ากันของ set)
pets_copy = {"dog", "cat", "rabbit"}
print(f"Are pets equal to pets_copy? {pets == pets_copy}")      # เท่ากันหรือไม่

# Length and membership (จำนวน element และตรวจสอบสมาชิก)
print(f"Number of mammals: {len(mammals)}")
print(f"Is 'dog' in mammals? {'dog' in mammals}")
print(f"Is 'fish' in mammals? {'fish' in mammals}")


""""
Summ.
    .issubset(other_set) → ตรวจสอบว่า set เป็น subset ของอีก set หรือไม่

    .issuperset(other_set) → ตรวจสอบว่า set เป็น superset ของอีก set หรือไม่

    .isdisjoint(other_set) → ตรวจสอบว่าไม่มี element ร่วมกัน

    == → ตรวจสอบ equality ของ set

    len(set) → จำนวน element

    'value' in set → ตรวจสอบ membership
"""