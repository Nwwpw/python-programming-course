"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
    
    #Private attributes for length and width
    def __init__(self, length, width):
        self.__length = length  # Private attribute (กำหนดความยาว), __หลัง.คือทำให้เป็นprivate
        self.__width = width   # Private attribute (กำหนดความกว้าง), __หลัง.คือทำให้เป็นprivate
    """
    หรือทำแบบนี้ก็ได้ กำหนดตามโจทย์แค่ฝั่งซ้าย
    def __init__(self, x, y):
        self.__length = x  # Private attribute (กำหนดความยาว), __หลัง.คือทำให้เป็นprivate
        self.__width = y   # Private attribute (กำหนดความกว้าง), __หลัง.คือทำให้เป็นprivate
    """

    #Methods to calculate area (getArea()) and perimeter getPerimeter())
    def getArea(self):
        area = self.__length * self.__width     # พื้นที่ = ความยาว x ความกว้าง
        return f"Area = {area}"
    def getPerimeter(self):
        perimeter = 2 * (self.__length + self.__width)   # เส้นรอบรูป = 2 x (ความยาว + ความกว้าง)
        return f"Perimeter = {perimeter}"
    
    #A method to check if it's a square (isSquare())
    def isSquare(self):
        if self.__length == self.__width:    # ถ้าความยาวเท่ากับความกว้าง จะเป็นสี่เหลี่ยมจัตุรัส
            return f"This rectangle is square"
        else:
            return f"This rectangle is not square"
        """
        --or--
        if self.__length == self.__width:    # ถ้าความยาวเท่ากับความกว้าง จะเป็นสี่เหลี่ยมจัตุรัส
            return TRUE
        else:
            return FALSE
        """

#How to use
rectangle = Rectangle(10, 5)
print(rectangle.getArea())   #Area = 50
rectangle.getPerimeter()
print(rectangle.isSquare())  #This rectangle is not square