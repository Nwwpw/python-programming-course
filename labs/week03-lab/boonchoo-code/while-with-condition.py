# Example 1: Input validation with while loop
while True:
    user_input = input("Enter a positive number: ")
    try:
        number = float(user_input)
        if number > 0:
            print(f"Thank you! You entered: {number}")
            break
        else:
            print("Please enter a positive number!") #ถ้าuserกรอกค่าติดลบ จะให้กรอกเลขที่มีค่าบวก
    except ValueError:
        print("That's not a valid number!")

# Example 2: Menu system
while True:
    print("\n=== Main Menu ===")
    print("1. Calculate Circle Area")
    print("2. Calculate Rectangle Area") #สี่เหลี่ยม
    print("3. Calculate Triangle Area") #สามเหลี่ยม
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        radius = float(input("Enter radius: ")) #radius=รัศมี
        if radius > 0:
            area = 3.14159 * radius * radius
            print(f"Circle area: {area:.2f}")
        else:
            print("Radius must be positive!") #รัศมีต้องเป็นค่าบวก(โปรแกรมที่ดีควรตรวจ เพราะค่าติดลบไม่ได้)
            
    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        if length > 0 and width > 0:
            area = length * width
            print(f"Rectangle area: {area:.2f}")
        else:
            print("Length and width must be positive!")
            
    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        if base > 0 and height > 0:
            area = 0.5 * base * height
            print(f"Triangle area: {area:.2f}")
        else:
            print("Base and height must be positive!")
            
    elif choice == "4":
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid choice! Please enter 1-4.")