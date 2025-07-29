"""
Personal Information Manager > ตัวจัดการข้อมูลสารสนเทศส่วนบุคคล

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Namwan", 19, "Bangkok", "Thailand")  # name, age, city, country
    hobbies = []
    while True:
        choice = input("Please select (1.Display all information, 2.Add new hobbies, 3.Remove hobbies, 4.Update age, 5.Exit: ): ")
        
        # Your code here
        if choice == "1":
            #Display all information
            print("Name: ", person[0]) #ตรงpersonเป็น person[-4] ก็ได้
            print("Age: ",person[1])
            print("City: ",person[-2])
            print("Country: ",person[-1])
            print("Hobbies: ",hobbies)

        elif choice == "2":
            #Add new hobbies
            hobby = input("What is your hobby?: ")
            hobbies.append(hobby)

        elif choice == "3":
            #Remove hobbies
            del hobbies[0]

        elif choice == "4":
            #Update age (by creating a new tuple) / Edit age
            person_list = list(person)
            age = int(input("How old are you?: "))
            person_list[1]= age
            person = tuple(person_list)

        elif choice == "5":
            break

if __name__ == "__main__":
        personal_info_manager()