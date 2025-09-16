""" 
Create a class hierarchy(ลำดับชั้น):

    Base class Vehicle with attributes: brand, model, year
    Derived class(คลาสที่สืบทอด) Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes (ใช้วิธี get_info() ทั้งสองคลาส)
(ดูไฟล์Animal ช่วย)
"""

class Vehicle:  # คลาสหลัก
    
    # Base class Vehicle with attributes: brand, model, year
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    # Implement a method get_info() in both classes
    def get_info(self):
         return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):   # คลาสลูก สืบทอดจาก Vehicle เหมือน Dog สืบทอดจาก Animal (Animal.py)
    
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
    
    # Implement a method get_info() in both classes
    def get_info(self):
         return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Doors: {self.number_of_doors}"

#How to use
myCar = Car("Toyota", "Prius", 2022, 5)
print(myCar.get_info())     # Brand: Toyota, Model: Prius, Year: 2022, Doors: 5